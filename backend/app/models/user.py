# from app.models.levels import Phase
from enum import IntEnum
from typing import List, Union, Dict
import uuid

from pydantic import Field, validator

from .base import Base, ObjectID
from .levels import Level, Phase


class Finance(Base):
    """Financial aspect of a user"""
    current: float = 20000
    expenditure: float = 5000
    salary: float = 10000.0
    debt: float = 0.0
    bank: float = 6
    interest: float = 3.5


class Insurance(Base):
    """Flags to check whether insurance has been taken"""
    house: bool = False
    individualHealth: bool = False
    familyHealth: bool = False
    # car: bool = False         # Not for our target audience 
    life: bool = False
    pensionFund: bool = False


class State(Base):
    """State to save the user progress"""
    code: uuid.UUID
    insurance: Insurance = Insurance()
    finances: Finance = Finance()
    completed: List[Level] = list()
    remaining: List[Level] = list()
    current: Phase = Phase.phase1
