from enum import Enum, IntEnum
from typing import List, Dict, Union, Optional

from pydantic import Field

from .base import Base, ObjectID


class Phase(IntEnum):
    """Phases of the gameplay"""
    phase1 = 1
    phase2 = 2
    phase3 = 3
    phase4 = 4


class Event(Base):
    """Event modification when, and if, an action is performed"""
    id: int
    probability: Optional[float] = 0.0
    phase: Optional[int]


class Action(Base):
    """Action to be performed on the selection of an option"""
    expenditure: float = 0.0        # Add this amount to expenditure
    debt: float = 0.0
    current: float = 0.0            # Add this amount to current (if negative value, will get subtracted)
    salary: float = 0.0             # Add this amount to salary
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
    # id: ObjectID = Field(None, alias="_id")
    # int_id: int = Field(None, alias="id")
    id: int
    title: Optional[str]
    description: Dict[str, str] = dict()
    image: Optional[str]

    options: List[Option] = list()
    probability: float = 0.0
    # phase: Union[Phase, List[Phase]]
    phase: int

    audio: Dict[str, str] = dict()
