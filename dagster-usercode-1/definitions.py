from dagster import Definitions
from assets import *

defs = Definitions(
    assets=[asset1],
    schedules=[],
    sensors=[],
    resources={},
)