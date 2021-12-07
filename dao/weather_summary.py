from dataclasses import dataclass


@dataclass
class WeatherSummary:
    symbol_code: str
    symbol_confidence: str


@dataclass
class WeatherDetails:
    probability_of_precipitation: float
