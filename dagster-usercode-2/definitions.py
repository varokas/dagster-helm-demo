from dagster import Definitions
from assets import *

defs = Definitions(
    assets=[asset2],
    schedules=[],
    sensors=[],
    resources={},
)
