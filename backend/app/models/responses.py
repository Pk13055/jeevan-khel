from typing import Optional, List, Dict, Union

from .base import Base
from .user import Finance, State

import uuid


class ResponseBase(Base):
    success: bool = True
    error: Optional[List]
    data: Optional[Union[List, Dict[str, str]]]


class StateInResponse(ResponseBase):
    data: State
    

class UserAction(Base):
    # code: uuid.UUID
    # code: str
    level_id: int
    option_id: int
