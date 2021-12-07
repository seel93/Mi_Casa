from dataclasses import dataclass
from datetime import datetime

@dataclass
class DayInterval:
    start: datetime
    end: datetime
    twentyFourHourSymbol: str
    symbolConfidence: str


@dataclass
class Precipitation:
    value: int
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


@dataclass
class LocationForecast:
    dayInterval: DayInterval
    precipitation: Precipitation
    temperature: Temperature
    wind: Wind

