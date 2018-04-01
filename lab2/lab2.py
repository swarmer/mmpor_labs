#!/usr/bin/env python
from bisect import bisect_left
import json

import numpy as np
from ortools.graph import pywrapgraph


def main():
    with open('data.json') as infile:
        data = json.load(infile)

    costs = (
        -np.array(data['efficiency'])
        .repeat(data['group_sizes'], axis=0)
        .repeat(data['work_sizes'], axis=1)
    )
    assignment = pywrapgraph.LinearSumAssignment()
    for (i, j), cost in np.ndenumerate(costs):
        assignment.AddArcWithCost(i, j, int(cost))

    solve_status = assignment.Solve()
    if solve_status == assignment.OPTIMAL:
        print(f'Total efficiency: {-assignment.OptimalCost()}')
        print()

        for i in range(assignment.NumNodes()):
            task = assignment.RightMate(i)
            efficiency = -assignment.AssignmentCost(i)
            worker_group = bisect_left(np.cumsum(data['group_sizes']) - 1, i)
            work_group = bisect_left(np.cumsum(data['work_sizes']) - 1, task)
            print(f'Worker from group {worker_group} assigned to task group {work_group}, efficiency: {efficiency}')
    elif solve_status == assignment.INFEASIBLE:
        print('Assignment is impossible')
    elif solve_status == assignment.POSSIBLE_OVERFLOW:
        print('Possible overflow')


if __name__ == '__main__':
    main()
