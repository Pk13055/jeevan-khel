from typing import Optional, List, Dict, Union

from .base import Base
from .user import State


class ResponseBase(Base):
    success: bool = True
    error: Optional[List]
    data: Optional[Union[List, Dict[str, str]]]


class StateInResponse(ResponseBase):
    data: State
