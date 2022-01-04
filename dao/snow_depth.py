from dataclasses import dataclass, field
from dataclasses_json import dataclass_json


@dataclass
class Region:
    id: str
    name: str


@dataclass
class Snow:
    time: str
    depth: int


@dataclass
class SnowDepth:
    time: str
    depth: int


@dataclass
class Category:
    id: str
    name: str


@dataclass
class Position:
    lat: float
    lon: float


@dataclass
class Country:
    id: str
    name: str


@dataclass
class Region:
    id: str
    name: str


@dataclass
class SubRegion:
    id: str
    name: str


@dataclass
class Location:
    category: Category
    id: str
    name: str
    position: Position
    elevation: int
    timeZone: str
    urlPath: str
    country: Country
    region: Region
    subregion: SubRegion


@dataclass(unsafe_hash=True)
class Station:
    snow: Snow
    snowDepths: [SnowDepth] = field(default_factory=list, init=False, compare=False, hash=False)
    name: str
    stationId: str
    validFrom: str
    location: Location


@dataclass_json
@dataclass(unsafe_hash=True)
class SnowDepthReport:
    region: Region
    #dates: [str] = field(default_factory=list, init=False, compare=False, hash=False)
    #stations: [Station] = field(default_factory=list, init=False, compare=False, hash=False)
