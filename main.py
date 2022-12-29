
from ortools.linear_solver import pywraplp

from driving_solution_collector import DrivingSolutionCollector

DrivingSolutionCollector
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        exit(1)

    x = solver.NumVar(0, 1, 'x')
    y = solver.NumVar(0, 2, 'y')

    print(f'Number of variables: {solver.NumVariables()}')

    ct = solver.Constraint(0, 2,'ct')
    ct.SetCoefficient(x, 1)
    ct.SetCoefficient(y, 1)

    print('Number of constraints =', solver.NumConstraints())

    objective = solver.Objective()
    objective.SetCoefficient(x, 3)
    objective.SetCoefficient(y, 1)
    objective.SetMaximization()


    solver.Solve()
    print('Solution:')
    print(f'Objective value = {objective.Value()}')
    print('x =', x.solution_value())
    print('y =', y.solution_value())




