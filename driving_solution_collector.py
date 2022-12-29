from typing import Tuple, List

from ortools.sat.python import cp_model

from driving_plan import DrivingPlan

class DrivingSolutionCollector(cp_model.CpSolverSolutionCallback):
    def __init__(self, limit: int, num_families: int, num_weekends: int, drivingVars: List[Tuple[int, int]]):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self._limit = limit
        self.solutions = []
        self.num_families = num_families
        self.num_weekends = num_weekends
        self.drivingVars = drivingVars
        self._count = 0

    def on_solution_callback(self):
        self._count += 1
        solutionDrivings = []
        for i in range(0, self.num_families):
            for j in range(0, self.num_weekends):
                if self.Value(self.drivingVars[(i, j)]):
                    solutionDrivings.append((i, j))
        self.solutions.append(DrivingPlan(drivings=solutionDrivings))

        if self._count >= self._limit:
            self.StopSearch()

