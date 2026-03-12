from searching_framework.utils import Problem
from searching_framework.uninformed_search import breadth_first_graph_search
from searching_framework.informed_search import astar_search
import time

class House_Problem(Problem):

    def __init__(self, initial, house, grid):
        super().__init__(initial)
        self.house = house
        self.grid = grid

    def goal_test(self, state):
        man = state[0]
        return man == self.house

    def move_obstacle(self, o):
        ox, oy, odir = o
        if odir == 'down':
            new_ox, new_oy = ox, oy - 1
            if new_oy >= 0:
                return new_ox, new_oy, odir
            else:
                return ox, oy, 'up'
        else:  # odir == 'up'
            new_ox, new_oy = ox, oy + 1
            if new_oy < self.grid[1]:
                return new_ox, new_oy, odir
            else:
                return ox, oy, 'down'

    def check_valid(self, m, o1, o2):
        nmx, nmy = m
        no1 = o1
        no2 = o2
        return ((nmx, nmy) != (no1[0], no1[1]) and
            (nmx, nmy) != (no2[0], no2[1]) and
            0 <= nmx < self.grid[0] and
            0 <= nmy < self.grid[1])


    def successor(self, state):
        successors = {}

        man, o1, o2 = state
        mx, my = man

        no1 = self.move_obstacle(o1)
        no2 = self.move_obstacle(o2)

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        actions = ['Right', 'Left', 'Up', 'Down']

        for (dx, dy), action in zip(directions, actions):
            nmx, nmy = mx + dx, my + dy
            if self.check_valid((nmx, nmy), no1, no2):
                successors[action] = ((nmx, nmy), no1, no2)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        state = node.state
        mx, my = state[0]
        hx, hy = self.house

        return abs(mx - hx) // 2 + abs(my - hy)


if __name__ == '__main__':
    mx, my = 0, 2
    o1x, o1y, o1dir = 2, 5, 'down'
    o2x, o2y, o2dir = 5, 0, 'up'
    hx, hy = 7, 4
    gx, gy = 8, 6

    initial = ((mx, my), (o1x, o1y, o1dir), (o2x, o2y, o2dir))
    house = hx, hy
    grid = gx, gy
    problem = House_Problem(initial, house, grid)

    # print(breadth_first_graph_search(problem).solution())
    print(astar_search(problem).solution())



