"""
@author yaoxs@shukun.net
@date 2019/11/14 14:35
"""
from dataclasses import dataclass
from dataclasses import asdict, astuple


@dataclass
class Lang:
    """use dataclass wrapper to describe a programing language"""
    name: str = "python"
    strong_type: bool = True
    static_type: bool = False
    age: int = 20


if __name__ == "__main__":
    lang = Lang()
    print(lang)
    print(lang == Lang("python", True, False, 20))
    print(asdict(lang))
    print(astuple(lang))