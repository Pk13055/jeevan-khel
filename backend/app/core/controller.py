import uuid

from fastapi import APIRouter, Depends, Security
from motor.motor_asyncio import AsyncIOMotorClient

from ..utils.mongodb import get_database
from ..models.responses import StateInResponse
from ..models.levels import Level
from ..models.user import State


router = APIRouter()


@router.get("/new", response_model=StateInResponse)
async def get_game_code(resume: uuid.UUID = None, db: AsyncIOMotorClient = Depends(get_database)) -> StateInResponse:
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
    else:
        state = State(**_state)
    return StateInResponse(data=state)