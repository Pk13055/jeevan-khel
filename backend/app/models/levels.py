from enum import Enum, IntEnum
from typing import List, Dict

from pydantic import Field

from .base import Base, ObjectID


class TransType(Enum):
    EN = 'en'
    HI = 'hi'
    MH = 'mh'


class Phase(IntEnum):
    """Phases of the gameplay"""
    phase1 = 1
    phase2 = 2
    phase3 = 3
    phase4 = 4


class Event(Base):
    """Event modification when, and if, an action is performed"""
    id: ObjectID
    probability: float = 0.0
    phase: Phase


class Action(Base):
    """Action to be performed on the selection of an option"""
    expenditure: float = 0.0
    debt: float = 0.0
    current: float = 0.0
    events: List[Event] = list()


class Option(Base):
    """Option for a given level"""
    description: str
    action: Action

    translation: Dict[TransType, str] = dict()
    audio: Dict[TransType, str] = dict()


class Level(Base):
    """Level object that contains the information for a given level"""
    id: ObjectID = Field(None, alias="_id")
    title: str
    description: str
    image: str

    options: List[Option] = list()
    probability: float = 1.0
    phase: Phase

    translation: Dict[TransType, str] = dict()
    audio: Dict[TransType, str] = dict()
