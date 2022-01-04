from dataclasses import dataclass
from datetime import datetime
from dataclasses_json import dataclass_json


@dataclass
class Summary:
    symbol_code: str
    symbol_confidence: str


@dataclass
class Details:
    probability_of_precipitation: float


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



@dataclass
class Precipitation:
    value: float
    probability: int


@dataclass
class Temperature:
    value: float
    min: float
    max: float


@dataclass
class Wind:
    min: float
    max: float
    maxGust: float = 0.0


@dataclass_json
@dataclass
class LocationForecast:
    start: str
    end: str
    twentyFourHourSymbol: str
    #twelveHourSymbols: [str]
    #sixHourSymbols: [str]
    #symbolConfidence: str
    precipitation: Precipitation
    temperature: Temperature
    wind: Wind
