from enum import Enum, IntEnum
from typing import List, Dict, Union, Optional

from pydantic import Field

from .base import Base, ObjectID


# class TransType(Enum):
#     EN = 'EN'
#     HI = 'HI'
#     MH = 'MH'

#     def __repr__(self):
#         return str(self.value)

#     def __str__(self):
#         return str(self.value)


class Phase(IntEnum):
    """Phases of the gameplay"""
    phase1 = 1
    phase2 = 2
    phase3 = 3
    phase4 = 4


class Event(Base):
    """Event modification when, and if, an action is performed"""
    id: ObjectID
    probability: Optional[float] = 0.0
    phase: Optional[Phase]


class Action(Base):
    """Action to be performed on the selection of an option"""
    expenditure: float = 0.0
    debt: float = 0.0
    current: float = 0.0
    events: List[Event] = list()


class Option(Base):
    """Option for a given level"""
    id: int
    description: str
    action: Action

    translation: Dict[str, str] = dict()
    audio: Dict[str, str] = dict()


class Level(Base):
    """Level object that contains the information for a given level"""
    id: ObjectID = Field(None, alias="_id")
    title: str
    description: str
    image: str

    options: List[Option] = list()
    probability: float = 1.0
    phase: Union[Phase, List[Phase]]

    translation: Dict[str, str] = dict()
    audio: Dict[str, str] = dict()
