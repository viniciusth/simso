from .IntegerACET import IntegerACET
from .WCET import WCET
from .ACET import ACET
from .CacheModel import CacheModel
from .FixedPenalty import FixedPenalty

execution_time_models = {
    "wcet": WCET,
    "acet": ACET,
    "iacet": IntegerACET,
    "cache": CacheModel,
    "fixedpenalty": FixedPenalty,
}

execution_time_model_names = {
    "WCET": "wcet",
    "ACET": "acet",
    "IACET": "iacet",
    "Cache Model": "cache",
    "Fixed Penalty": "fixedpenalty",
}
