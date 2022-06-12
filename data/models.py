import typing as t

from enum import Enum
from dataclasses import dataclass, field


__all__ = ['Rarity', 'Powerup', 'Driver', 'Track', 'Course', 'Cup', 'Tour']


class Rarity(Enum):
    COMMON = 'Common'
    SUPER = 'Super'
    HIGH_END = 'High End'



@dataclass
class Powerup:
    name: str
    description: str

    plus_description: t.Optional[str] = None
    special: bool = False



@dataclass
class Driver:
    name: str
    special_powerup: Powerup
    level: int = 1

    rarity: Rarity = field(default=Rarity.COMMON)


    def lvl(self, level: int = 1) -> 'Driver':
        d = self
        d.level = level

        return d



@dataclass
class Track:
    name: str
    two_item_slot_drivers: t.List[Driver] = field(default_factory=list)
    three_item_slot_drivers: t.List[Driver] = field(default_factory=list)



class Course:
    def __init__(self, track: Track, favored_driver: Driver, is_bonus: bool = False):
        self.track = track
        self.favored_driver = favored_driver
        self.is_bonus = is_bonus

        self.two_item_slot_drivers = self.track.two_item_slot_drivers
        self.three_item_slot_drivers = self.track.three_item_slot_drivers

        if self.favored_driver not in self.three_item_slot_drivers:
            self.three_item_slot_drivers.append(self.favored_driver)



@dataclass
class Cup:
    name: str
    favored_driver: Driver
    courses: t.Tuple[Course, Course, Course, Course] = field(default_factory=list)    


    def __post__init__(self):
        for course in self.courses:
            if self.favored_driver != course.favored_driver and self.favored_driver not in course.three_item_slot_drivers:
                course.two_item_slot_drivers.append(self.favored_driver)



@dataclass
class Tour:
    name: str
    cups: t.List[Cup] = field(default_factory=list)
