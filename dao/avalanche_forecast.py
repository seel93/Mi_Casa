from dataclasses import dataclass
from dataclasses_json import dataclass_json
from datetime import datetime


@dataclass_json
@dataclass
class AvalancheReport:
    RegId: int
    RegionId: int
    RegionName: str
    RegionTypeId: int
    DangerLevel: str
    ValidFrom: str
    ValidTo: str
    NextWarningTime: str
    PublishTime: str
    MainText: str
    LangKey: int
