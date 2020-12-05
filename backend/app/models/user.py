from enum import IntEnum, Enum
from typing import List, Union, Dict, Optional
import uuid

from pydantic import Field, validator

from .base import Base, ObjectID
from .levels import Level, Phase


class Gender(str, Enum):
    male = 'male'
    female = 'female'


class Finance(Base):
    """Financial aspect of a user"""
    current: float = 0.0
    expenditure: float = 0.0
    salary: float = 0.0
    debt: float = 0.0
    bank: float = 6.0
    interest: float = 3.5


class Insurance(Base):
    """Flags to check whether insurance has been taken"""
    # house: bool = False
    individualHealth: bool = False
    familyHealth: bool = False
    parentsHealth: bool = False
    life: bool = False
    accident: bool = False
    pensionFund: bool = False
    pensionAmount: int = 0


class State(Base):
    """State to save the user progress"""
    token: Optional[str]
    code: uuid.UUID
    gender: str
    insurance: Insurance = Insurance()
    finances: Finance = Finance()
    completed: List[Level] = list()
    remaining: List[Level] = list()
    current: Level