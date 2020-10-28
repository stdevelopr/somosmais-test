# Model data structure and validate types

from dataclasses import dataclass
from dataclass_type_validator import dataclass_type_validator
from typing import List

@dataclass
class Name:
    title: str
    first: str
    last: str

    def __post_init__(self):
        dataclass_type_validator(self)

@dataclass
class Coordinates:
    latitude: float
    longitude: float

    def __post_init__(self):
        dataclass_type_validator(self)

@dataclass
class Timezone:
    offset: str
    description: str

    def __post_init__(self):
        dataclass_type_validator(self)

@dataclass
class Location:
    region: str
    street: str
    city: str
    state: str
    postcode: int
    coordinates: Coordinates
    timezone: Timezone

    def __post_init__(self):
        dataclass_type_validator(self)

@dataclass
class Picture:
    large: str
    medium: str
    thumbnail: str

    def __post_init__(self):
        dataclass_type_validator(self)

@dataclass
class Client:
    type: str
    gender: str
    name: Name
    location: Location
    email: str
    birthday: str
    registered: str
    telephoneNumbers: List[str]
    mobileNumbers: List[str]
    picture: Picture
    nationality: str

    def __post_init__(self):
        dataclass_type_validator(self)