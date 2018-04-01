#!/usr/bin/env python
from ortools.linear_solver import pywraplp


class Timetable:
    def __init__(self):
        solver = self.solver = pywraplp.Solver(
            'SolveIntegerProblem',
            pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING,
        )
        self.optimal = None
        self.verified = None

        f1 = self.f1 = solver.IntVar(0, solver.Infinity(), 'f1')  # fulltime 1, 9-12, 13-17, 8/h
        f2 = self.f2 = solver.IntVar(0, solver.Infinity(), 'f2')  # fulltime 2,  11-14, 15-19, 8/h
        p1 = self.p1 = solver.IntVar(0, solver.Infinity(), 'p1')  # parttime 1, 9-13, 6/h
        p2 = self.p2 = solver.IntVar(0, solver.Infinity(), 'p2')  # parttime 2, 10-14, 7/h
        p3 = self.p3 = solver.IntVar(0, solver.Infinity(), 'p3')  # parttime 3, 11-15, 9/h
        p4 = self.p4 = solver.IntVar(0, solver.Infinity(), 'p4')  # parttime 4, 12-16, 10/h
        p5 = self.p5 = solver.IntVar(0, solver.Infinity(), 'p5')  # parttime 5, 13-17, 8/h
        p6 = self.p6 = solver.IntVar(0, solver.Infinity(), 'p6')  # parttime 6, 14-18, 6/h
        p7 = self.p7 = solver.IntVar(0, solver.Infinity(), 'p7')  # parttime 7, 15-19, 6/h
        self.variables = [f1, f2, p1, p2, p3, p4, p5, p6, p7]

        constraint_9_10 = self.constraint_9_10 = solver.Constraint(16, solver.Infinity())
        constraint_9_10.SetCoefficient(f1, 1)
        constraint_9_10.SetCoefficient(f2, 0)
        constraint_9_10.SetCoefficient(p1, 1)
        constraint_9_10.SetCoefficient(p2, 0)
        constraint_9_10.SetCoefficient(p3, 0)
        constraint_9_10.SetCoefficient(p4, 0)
        constraint_9_10.SetCoefficient(p5, 0)
        constraint_9_10.SetCoefficient(p6, 0)
        constraint_9_10.SetCoefficient(p7, 0)

        constraint_10_11 = self.constraint_10_11 = solver.Constraint(30, solver.Infinity())
        constraint_10_11.SetCoefficient(f1, 1)
        constraint_10_11.SetCoefficient(f2, 0)
        constraint_10_11.SetCoefficient(p1, 1)
        constraint_10_11.SetCoefficient(p2, 1)
        constraint_10_11.SetCoefficient(p3, 0)
        constraint_10_11.SetCoefficient(p4, 0)
        constraint_10_11.SetCoefficient(p5, 0)
        constraint_10_11.SetCoefficient(p6, 0)
        constraint_10_11.SetCoefficient(p7, 0)

        constraint_11_12 = self.constraint_11_12 = solver.Constraint(31, solver.Infinity())
        constraint_11_12.SetCoefficient(f1, 1)
        constraint_11_12.SetCoefficient(f2, 1)
        constraint_11_12.SetCoefficient(p1, 1)
        constraint_11_12.SetCoefficient(p2, 1)
        constraint_11_12.SetCoefficient(p3, 1)
        constraint_11_12.SetCoefficient(p4, 0)
        constraint_11_12.SetCoefficient(p5, 0)
        constraint_11_12.SetCoefficient(p6, 0)
        constraint_11_12.SetCoefficient(p7, 0)

        constraint_12_13 = self.constraint_12_13 = solver.Constraint(45, solver.Infinity())
        constraint_12_13.SetCoefficient(f1, 0)
        constraint_12_13.SetCoefficient(f2, 1)
        constraint_12_13.SetCoefficient(p1, 1)
        constraint_12_13.SetCoefficient(p2, 1)
        constraint_12_13.SetCoefficient(p3, 1)
        constraint_12_13.SetCoefficient(p4, 1)
        constraint_12_13.SetCoefficient(p5, 0)
        constraint_12_13.SetCoefficient(p6, 0)
        constraint_12_13.SetCoefficient(p7, 0)

        constraint_13_14 = self.constraint_13_14 = solver.Constraint(66, solver.Infinity())
        constraint_13_14.SetCoefficient(f1, 1)
        constraint_13_14.SetCoefficient(f2, 1)
        constraint_13_14.SetCoefficient(p1, 0)
        constraint_13_14.SetCoefficient(p2, 1)
        constraint_13_14.SetCoefficient(p3, 1)
        constraint_13_14.SetCoefficient(p4, 1)
        constraint_13_14.SetCoefficient(p5, 1)
        constraint_13_14.SetCoefficient(p6, 0)
        constraint_13_14.SetCoefficient(p7, 0)

        constraint_14_15 = self.constraint_14_15 = solver.Constraint(72, solver.Infinity())
        constraint_14_15.SetCoefficient(f1, 1)
        constraint_14_15.SetCoefficient(f2, 0)
        constraint_14_15.SetCoefficient(p1, 0)
        constraint_14_15.SetCoefficient(p2, 0)
        constraint_14_15.SetCoefficient(p3, 1)
        constraint_14_15.SetCoefficient(p4, 1)
        constraint_14_15.SetCoefficient(p5, 1)
        constraint_14_15.SetCoefficient(p6, 1)
        constraint_14_15.SetCoefficient(p7, 0)

        constraint_15_16 = self.constraint_15_16 = solver.Constraint(61, solver.Infinity())
        constraint_15_16.SetCoefficient(f1, 1)
        constraint_15_16.SetCoefficient(f2, 1)
        constraint_15_16.SetCoefficient(p1, 0)
        constraint_15_16.SetCoefficient(p2, 0)
        constraint_15_16.SetCoefficient(p3, 0)
        constraint_15_16.SetCoefficient(p4, 1)
        constraint_15_16.SetCoefficient(p5, 1)
        constraint_15_16.SetCoefficient(p6, 1)
        constraint_15_16.SetCoefficient(p7, 1)

        constraint_16_17 = self.constraint_16_17 = solver.Constraint(34, solver.Infinity())
        constraint_16_17.SetCoefficient(f1, 1)
        constraint_16_17.SetCoefficient(f2, 1)
        constraint_16_17.SetCoefficient(p1, 0)
        constraint_16_17.SetCoefficient(p2, 0)
        constraint_16_17.SetCoefficient(p3, 0)
        constraint_16_17.SetCoefficient(p4, 0)
        constraint_16_17.SetCoefficient(p5, 1)
        constraint_16_17.SetCoefficient(p6, 1)
        constraint_16_17.SetCoefficient(p7, 1)

        constraint_17_18 = self.constraint_17_18 = solver.Constraint(16, solver.Infinity())
        constraint_17_18.SetCoefficient(f1, 0)
        constraint_17_18.SetCoefficient(f2, 1)
        constraint_17_18.SetCoefficient(p1, 0)
        constraint_17_18.SetCoefficient(p2, 0)
        constraint_17_18.SetCoefficient(p3, 0)
        constraint_17_18.SetCoefficient(p4, 0)
        constraint_17_18.SetCoefficient(p5, 0)
        constraint_17_18.SetCoefficient(p6, 1)
        constraint_17_18.SetCoefficient(p7, 1)

        constraint_18_19 = self.constraint_18_19 = solver.Constraint(10, solver.Infinity())
        constraint_18_19.SetCoefficient(f1, 0)
        constraint_18_19.SetCoefficient(f2, 1)
        constraint_18_19.SetCoefficient(p1, 0)
        constraint_18_19.SetCoefficient(p2, 0)
        constraint_18_19.SetCoefficient(p3, 0)
        constraint_18_19.SetCoefficient(p4, 0)
        constraint_18_19.SetCoefficient(p5, 0)
        constraint_18_19.SetCoefficient(p6, 0)
        constraint_18_19.SetCoefficient(p7, 1)

        self.constraints = [
            constraint_9_10, constraint_10_11, constraint_11_12, constraint_12_13, constraint_13_14,
            constraint_14_15, constraint_15_16, constraint_16_17, constraint_17_18, constraint_18_19,
        ]

        objective = self.objective = solver.Objective()
        objective.SetCoefficient(f1, 8 * 8)
        objective.SetCoefficient(f2, 8 * 8)
        objective.SetCoefficient(p1, 6 * 4)
        objective.SetCoefficient(p2, 7 * 4)
        objective.SetCoefficient(p3, 9 * 4)
        objective.SetCoefficient(p4, 10 * 4)
        objective.SetCoefficient(p5, 8 * 4)
        objective.SetCoefficient(p6, 6 * 4)
        objective.SetCoefficient(p7, 6 * 4)
        objective.SetMinimization()

    def solve(self):
        result = self.solver.Solve()
        self.optimal = result == pywraplp.Solver.OPTIMAL
        if self.optimal:
            self.verified = self.solver.VerifySolution(1e-4, True)


def show_solution(timetable: Timetable):
    print(f'Optimal: {timetable.optimal}')
    print(f'Verified: {timetable.verified}')

    if not timetable.optimal or not timetable.verified:
        return

    for variable in timetable.variables:
        print(f'{variable.name()}: {variable.solution_value()}')

    print(f'Objective: {timetable.objective.Value()}')


def main():
    # а)
    timetable = Timetable()
    timetable.solve()
    show_solution(timetable)
    print()

    # б)
    timetable = Timetable()
    fulltime_constraint = timetable.solver.Constraint(4, timetable.solver.Infinity())
    fulltime_constraint.SetCoefficient(timetable.f1, 1)
    fulltime_constraint.SetCoefficient(timetable.f2, 1)
    timetable.constraints.append(fulltime_constraint)
    timetable.solve()
    show_solution(timetable)
    print()

    # в)
    timetable = Timetable()
    count_constraint = timetable.solver.Constraint(0, 94)
    count_constraint.SetCoefficient(timetable.f1, 1)
    count_constraint.SetCoefficient(timetable.f2, 1)
    count_constraint.SetCoefficient(timetable.p1, 1)
    count_constraint.SetCoefficient(timetable.p2, 1)
    count_constraint.SetCoefficient(timetable.p3, 1)
    count_constraint.SetCoefficient(timetable.p4, 1)
    count_constraint.SetCoefficient(timetable.p5, 1)
    count_constraint.SetCoefficient(timetable.p6, 1)
    count_constraint.SetCoefficient(timetable.p7, 1)
    timetable.constraints.append(count_constraint)
    timetable.solve()
    show_solution(timetable)


if __name__ == '__main__':
    main()
