from pydantic import BaseModel, Field
from datetime import date
from enum import Enum


class RoleEnum(str, Enum):
    ASSASSIN = "암살자"
    FIGHTER = "전사"
    MARKSMAN = "원거리"
    MAGE = "마법사"
    TANK = "탱커"
    SUPPORT = "서포터"


class Champion(BaseModel):
    id: int
    name: str = Field(..., min_length=2, max_length=50)
    release_date: date
    role: RoleEnum