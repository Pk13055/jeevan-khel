import uuid
import random
from typing import Dict

from fastapi import APIRouter, Depends, Security
from jose import jwt
from motor.motor_asyncio import AsyncIOMotorClient

from config import SECRET_KEY
from ..utils.mongodb import get_database
from ..utils.token import verify_token

from ..models.responses import StateInResponse, UserAction, FinanceUpdate
from ..models.levels import Level
from ..models.user import Gender, State, Finance
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
        firstLevel = None
        levels = []
        async for _level in db.core.levels.find():
            level = Level(**_level)
            levels.append(level)
            if level.id == 0:
                firstLevel = level
        state = State(code=code, gender=gender.value, current=firstLevel, remaining=levels)
        db.core.states.insert_one(state.dict())
    else:
        state = State(**_state)

    state.token = jwt.encode({'code': str(state.code)}, str(
        SECRET_KEY), algorithm="HS256")

    return StateInResponse(data=state)





@router.post("/update", response_model=StateInResponse)
async def change_state(game_state: UserAction, code: Dict[str, uuid.UUID] = Depends(verify_token),
                        db: AsyncIOMotorClient = Depends(get_database)) -> StateInResponse:
    _state = await db.core.states.find_one(code)
    state = State(**_state)
    current: Level = None
    for level in state.remaining:
        if level.id == game_state.level_id:
            current = level
            break

    # move from remaining to completed
    state.remaining.remove(current)
    state.completed.append(current)

    # update finances
    for option in current.options:
        if option.id == game_state.option_id:
            # check if insurance present
            if (game_state.level_id in [14, 17]) and state.insurance.individualHealth:
                pass
            elif (game_state.level_id in [15]) and state.insurance.parentsHealth:
                pass
            elif (game_state.level_id in [14]) and state.insurance.accident:
                pass
            else:
                # else, apply finance changes
                state.finances.current += option.action.current
                state.finances.expenditure += option.action.expenditure
                state.finances.salary += option.action.salary

                if state.finances.current < 0:
                    state.finances.debt = abs(state.finances.current)
                    state.finances.current = 0


            # update other affected events
            for event in option.action.events:
                for level in state.remaining:
                    if level.id == event.id:
                        level.probability += event.probability

            # Checking for insurance
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

    # Determine the next event to be shown

    # state.current = random.choice(state.remaining)

    remEventsCurrentPhase = []

    currentPhase = state.current.phase

    for lvl in state.remaining:
        if lvl.phase == currentPhase and (lvl.probability > 0):
            remEventsCurrentPhase.append(lvl)

    if len(remEventsCurrentPhase) == 0:

        # Change phase

        currentPhase += 1

        for lvl in state.remaining:
            if lvl.phase == currentPhase and (lvl.probability > 0):
                remEventsCurrentPhase.append(lvl)
    
    if len(remEventsCurrentPhase) == 0:
        pass
        # Game ends here

    # state.current = random.choices(remEventsCurrentPhase, [lvl.probability for lvl in remEventsCurrentPhase])[0]

    state.current = random.choice(remEventsCurrentPhase)
    
    db.core.states.update_one(code, { "$set" : state.dict()})
    return StateInResponse(data=state.dict())




@router.post("/finances", response_model=StateInResponse)
async def update_finances(updatedFinances: FinanceUpdate, db: AsyncIOMotorClient = Depends(get_database), game_code: Dict[str, uuid.UUID] = Depends(verify_token)) -> StateInResponse:

    # since = 12      # 12 months

    _state = await db.core.states.find_one(game_code)
    state = State(**_state)

    state.finances = Finance(**updatedFinances.finances)

    # state.finances.current += ( since*state.finances.salary - since*state.finances.expenditure )

    db.core.states.update_one(game_code, { "$set" : state.dict()})

    return StateInResponse(data=state.dict())


