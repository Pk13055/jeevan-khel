import uuid

from fastapi import APIRouter, Depends, Security
from motor.motor_asyncio import AsyncIOMotorClient

from ..utils.mongodb import get_database
from ..models.responses import StateInResponse, UserAction
from ..models.levels import Level
from ..models.user import State
from ..models.base import ObjectID

router = APIRouter()


@router.get("/new", response_model=StateInResponse)
async def get_game_state(resume: uuid.UUID = None, db: AsyncIOMotorClient = Depends(get_database)) -> StateInResponse:
    """Generate a new meeting code

        - If code is user given, then return code AND state of game, if it exists
        - If code does not exist, then start new game with a new code
    """

    code = resume if resume is not None else uuid.uuid4()
    _state = await db.core.states.find_one({"code": code})
    if _state is None:
        # define new game variable
        state = State(code=code)
        levels = db.core.levels.find()
        state.remaining = [Level(**level) async for level in levels]
        db.core.states.insert_one(state.dict())
    else:
        state = State(**_state)
    return StateInResponse(data=state)




# @router.post("/update", response_model=StateInResponse)
# # async def change_state(game_state: State, level_id: ObjectID, option_id: int, db: AsyncIOMotorClient = Depends(get_database)) -> StateInResponse:
# async def change_state(game_state: UserAction, db: AsyncIOMotorClient = Depends(get_database)) -> StateInResponse:
    
    # if game_state is not None:

    #     all_states = db.core.states.find()

    #     use_this_state = None

    #     for some_state in all_states:
    #         if game_state.code == some_state.code:
    #             use_this_state = some_state

    #     game_levels = game_state.data.remaining

    #     current_level = None

    #     for lvl in game_levels:
    #         if lvl.id == level_id:
    #             current_level = lvl

    #     current_options = current_level.options

    #     option = None

    #     # update finances

    #     for option in current_options:
    #         if option.id == option_id:
    #             game_state.data.finances.current += option.action.current
    #             game_state.data.finances.expenditure += option.action.expenditure

    #     # update other affected events

    #     # move from remaining to completed

    #     # Update state in database

    #     db.core.states.update_one(
    #         {
    #             "code": game_state.data.code,
    #             "$set" : {"finances.current" : game_state.data.finances.current}
    #         }
    #     )

    #     return StateInResponse(data=game_state.data)
        

@router.post("/update")
async def testFunction(game_state: UserAction, db: AsyncIOMotorClient = Depends(get_database)):
    
    _level = await db.core.levels.find_one({
        "id": game_state.level_id,
        "options.id": game_state.option_id
    })

    if _level:

        level = Level(**_level)

        _state = await db.core.states.find_one({
            "code": game_state.code
        })

        if _state:
            state = State(**_state)

            # print(state)

            return {
                "contains":level in state.remaining
            }
    


    return game_state


