from searching_framework.utils import Problem
from searching_framework.uninformed_search import breadth_first_graph_search


class My_Problem(Problem):

    def __init__(self, initial, house, grid):
        super().__init__(initial)
        self.house = house
        self.grid = grid

    def goal_test(self, state):
        man, o1, o2 = state
        return man == self.house

    def move_object(self, o):
        ox, oy, odir = o
        m, n = self.grid

        if odir == 'down':
            if oy - 1 < 0:
                nox, noy, nodir = ox, oy + 1, 'up'
            else:
                nox, noy, nodir = ox, oy - 1, odir
        else:  # odir == 'up'
            if oy + 1 >= n:
                nox, noy, nodir = ox, oy - 1, 'down'
            else:
                nox, noy, nodir = ox, oy + 1, odir

        no = (nox, noy, nodir)
        return no

    def check_valid(self, state):
        gx, gy = self.grid
        mx, my = state[0]
        o1x, o1y, o1dir = state[1]
        o2x, o2y, o2dir = state[2]

        return (0 <= mx < gx
                and 0 <= my < gy
                and (mx, my) != (o1x, o1y)
                and (mx, my) != (o2x, o2y))


    def successor(self, state):
        successors = {}

        man, o1, o2 = state
        no1, no2 = self.move_object(o1), self.move_object(o2)

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        actions = ['Move right', 'Move left', 'Move up', 'Move down']

        for (dx, dy), action in zip(dirs, actions):
            mx, my = man
            nmx, nmy = mx + dx, my + dy
            nman = nmx, nmy
            nstate = (nman, no1, no2)
        if self.check_valid(nstate):
            successors[action] = nstate

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]



if __name__ == '__main__':
    man = tuple(map(int, input().split(',')))
    o1x, o1y, o1dir = input().split(',')
    o1x, o1y = int(o1x), int(o1y)
    o2x, o2y, o2dir = input().split(',')
    o2x, o2y = int(o2x), int(o2y)
    o1 = (o1x, o1y, o1dir)
    o2 = (o2x, o2y, o2dir)
    house = tuple(map(int, input().split(',')))
    grid = (8, 6)

    initial = (man, o1, o2)
    problem = My_Problem(initial, house, grid)

    print(breadth_first_graph_search(problem).solution())
