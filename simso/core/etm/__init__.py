from .IntegerACET import IntegerACET
from .WCET import WCET
from .ACET import ACET
from .CacheModel import CacheModel
from .FixedPenalty import FixedPenalty
from .ProportionACET import ProportionACET

execution_time_models = {
    "wcet": WCET,
    "acet": ACET,
    "iacet": IntegerACET,
    "pacet": ProportionACET,
    "cache": CacheModel,
    "fixedpenalty": FixedPenalty,
}

execution_time_model_names = {
    "WCET": "wcet",
    "ACET": "acet",
    "IACET": "iacet",
    "PACET": "pacet",
    "Cache Model": "cache",
    "Fixed Penalty": "fixedpenalty",
}
