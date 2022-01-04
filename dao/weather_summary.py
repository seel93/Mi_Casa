from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass
class WeatherSummary:
    symbol_code: str
    symbol_confidence: str


@dataclass
class WeatherDetails:
    probability_of_precipitation: float


@dataclass
class Summary:
    symbol_code: str
    symbol_confidence: str


@dataclass
class Details:
    probability_of_perception: float

@dataclass
class NextTwelveHours:
    summary: Summary
    details: Details

@dataclass
class Data:
    next_12_hours: NextTwelveHours

@dataclass_json
@dataclass
class LocationSummary:
    time: str
    data: Data
