from dataclasses import dataclass


@dataclass
class Snow:
    time: str
    depth: int


@dataclass
class Station:
    snow: Snow


@dataclass
class SnowDepth:
    name: str
    dates: [str]
    stations: [Station]
