from searching_framework.utils import Problem
from searching_framework.uninformed_search import breadth_first_graph_search

class Two_Jars_Problem(Problem):

    def __init__(self, initial, capacities, goal):
        super().__init__(initial, goal=goal)
        self.capacities = capacities
        self.goal = goal

    def goal_test(self, state):
        return state == self.goal

    def successor(self, state):
        j0, j1 = state
        c0, c1 = self.capacities

        successors = {}

        if j0 > 0:
            successors['Empty first jar'] = (0, j1)

        if j1 > 0:
            successors['Empty second jar'] = (j0, 0)

        if j0 < c0:
            successors['Fill first jar'] = (c0, j1)

        if j1 < c1:
            successors['Fill second jar'] = (j0, c1)

        delta0 = c0 - j0  # remaining empty space in jar 0
        for l in range(1, delta0 + 1):
            if l > j1:
                break
            successors[f'Fill {l} liters in first jar'] = (j0 + l, j1 - l)

        delta1 = c1 - j1  # remaining empty space in jar 1
        for l in range(1, delta1 + 1):
            if l > j0:
                break
            successors[f'Fill {l} liters in second jar'] = (j0 - l, j1 + l)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]



if __name__ == '__main__':
    j0, j1 = list(map(int, input().split(',')))  # This changes
    c0, c1 = list(map(int, input().split(',')))  # This is fixed
    g0, g1 = list(map(int, input().split(',')))  # This is the goal

    # state = (amount of liquid in first jar, amount of liquid in second jar)
    initial = (j0, j1)
    capacities = (c0, c1)
    goal = (g0, g1)

    problem = Two_Jars_Problem(initial, capacities, goal)
    print(breadth_first_graph_search(problem).solution())

