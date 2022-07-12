import random
import math

from simso.core.etm.ACET import ACET


class IntegerACET(ACET):
    def on_activate(self, job):
        self.executed[job] = 0
        # execution time is a integer proportion of the original.
        # to avoid multiple changes in the source code we use the
        # task variable 'et_stddev' to represent the minimum proportion we want.
        self.et[job] = (
            math.ceil(job.task.wcet * random.uniform(job.task.et_stddev, 1.0))
            * self.sim.cycles_per_ms
        )
