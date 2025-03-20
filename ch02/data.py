from typing import List

from ch02.model import Champion, RoleEnum

_champions = [
    Champion(
        id = 1,
        name = "베인",
        release_date="2010-05-11",
        role = RoleEnum.TANK

    ),
    Champion(
        id=2,
        name="블리츠크랭크",
        release_date="2009-09-02",
        role = RoleEnum.FIGHTER
    )
]

def get_champion() -> List[Champion]:
    return _champions