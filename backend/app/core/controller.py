import uuid

from fastapi import APIRouter, Depends, Security
from jose import jwt
from motor.motor_asyncio import AsyncIOMotorClient

from config import SECRET_KEY
from ..utils.mongodb import get_database
from ..models.responses import StateInResponse, UserAction
from ..models.levels import Level
from ..models.user import Gender, State
from ..models.base import ObjectID

router = APIRouter()


@router.get("/new", response_model=StateInResponse)
async def get_game_state(gender: Gender, code: uuid.UUID = None,
                        db: AsyncIOMotorClient = Depends(get_database)) -> StateInResponse:
    """Generate a new meeting code

        - If code is user given, then return code AND state of game, if it exists
        - If code does not exist, then start new game with a new code
    """
    code = code if code is not None else uuid.uuid4()
    _state = await db.core.states.find_one({"code": code})
    if _state is None:
        # define new game variable
        state = State(code=code, gender=gender.value)
        levels = db.core.levels.find()
        state.remaining = [Level(**level) async for level in levels]
        db.core.states.insert_one(state.dict())
    else:
        state = State(**_state)
    state.token = jwt.encode({'code': str(state.code)}, str(
        SECRET_KEY), algorithm="HS256")
    return StateInResponse(data=state)





@router.post("/update", response_model=StateInResponse)
async def change_state(game_state: UserAction, db: AsyncIOMotorClient = Depends(get_database)):
    
    # _level = await db.core.levels.find_one({          # The level info can get modified in state.remaining
    #     "id": game_state.level_id,                    # So, taking level info from state instead
    #     "options.id": game_state.option_id
    # })

    _state = await db.core.states.find_one({
            "code": game_state.code
        })

    if _state:

        state = State(**_state)

        _level = None

        for lvl in state.remaining:

            if lvl.id == game_state.level_id:
                _level = lvl

        if _level:

            current_options = _level.options

            # move from remaining to completed

            state.remaining.remove(_level)
            state.completed.append(_level)


            """
            TODO: An API route for updating finances according to time elapsed

            TODO: Increase salary and expenditure WHEN THE PHASE CHANGES -- Check the phase of the level/event, compare with previous phase?

            TODO: Check if the game is too easy -- if so, reduce salary

            """

            # update finances

            current_options = _level.options

            for option in current_options:
                
                if option.id == game_state.option_id:

                    # Checking if insurance was taken for injury/illness events, in that case, don't modify current
                    
                    if (game_state.level_id in [14, 17]) and state.insurance.individualHealth == True:
                        pass
                        # Finances not affected

                    elif (game_state.level_id in [15]) and state.insurance.parentsHealth == True:
                        pass
                        # Finances not affected
                    
                    elif (game_state.level_id in [14]) and state.insurance.accident == True:
                        pass
                        # Finances not affected

                    else:
                        state.finances.current += option.action.current
                        state.finances.expenditure += option.action.expenditure
                        state.finances.salary += option.action.salary

                    # update other affected events

                    affectedEvents = option.action.events

                    if len(affectedEvents) > 0:
                        for event in affectedEvents:
                            for i in range(len(state.remaining)):
                                if state.remaining[i].id == event.id:
                                    state.remaining[i].probability += event.probability

                    # Checking for insurance

                    # NOTE: Premium amount has already been added to expenditure

                    if (game_state.level_id in [23]) and ("Yes" in option.description):
                        state.insurance.accident = True
                    
                    if (game_state.level_id in [24, 26]) and ("Yes" in option.description):
                        state.insurance.life = True
                    
                    if (game_state.level_id in [25]) and ("Yes" in option.description) and ("individual" in option.description):
                        state.insurance.individualHealth = True

                    elif (game_state.level_id in [25]) and ("Yes" in option.description) and ("parents" in option.description):
                        state.insurance.parentsHealth = True
                        state.insurance.familyHealth = True

                    elif (game_state.level_id in [25]) and ("Yes" in option.description) and ("family" in option.description):
                        state.insurance.familyHealth = True
                    
                    if (game_state.level_id in [27, 28, 29]) and ("Yes" in option.description):
                        state.insurance.pensionFund = True

            # Update state in database

            for i in range(len(state.remaining)):
                state.remaining[i] = state.remaining[i].dict()

            for i in range(len(state.completed)):
                state.completed[i] = state.completed[i].dict()

            db.core.states.update_one(
                { "code": game_state.code },
                { 
                    "$set" : {
                                "finances.current" : state.finances.current,
                                "finances.expenditure" : state.finances.expenditure,
                                "finances.salary" : state.finances.salary,
                                "completed" : state.completed,
                                "remaining" : state.remaining,
                                "insurance.accident" : state.insurance.accident,
                                "insurance.life" : state.insurance.life,
                                "insurance.individualHealth" : state.insurance.individualHealth,
                                "insurance.familyHealth" : state.insurance.familyHealth,
                                "insurance.pensionFund" : state.insurance.pensionFund
                            }
                }
            )

            return StateInResponse(data=state)


