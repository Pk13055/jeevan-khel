from app.models.levels import Phase
from enum import IntEnum
from typing import List, Union, Dict
import uuid

from pydantic import Field, validator

from .base import Base, ObjectID
from .levels import Level, Phase


class Finance(Base):
    """Financial aspect of a user"""
    current: float = 20000
    expenditue: float = 5000
    debt: float = 0.0
    bank: float = 6
    interest: float = 3.5


class State(Base):
    """State to save the user progress"""
    code: uuid.UUID
    finances: Finance = Finance()
    completed: List[Level] = list()
    remaining: List[Level] = list()
    current: Phase = Phase.phase1
