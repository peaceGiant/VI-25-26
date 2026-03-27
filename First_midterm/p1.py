from searching_framework import *


class Laser(Problem):
    def __init__(self, initial, grid, target_pos, allowed):
        super().__init__(initial)

        self.N, self.M = grid
        self.target_pos = target_pos
        self.allowed = allowed

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        man_pos = state[0]
        target_pos = self.target_pos
        return man_pos == target_pos

    def check_valid(self, state):
        (x, y), t, (lx, ly) = state
        N, M = self.N, self.M

        if not (0 <= x < M and 0 <= y < N):
            return False

        if (x, y) not in self.allowed:
            return False

        if x != lx and y != ly and t == 5:
            return False

        return True


    def successor(self, state):
        successors = {}

        (x, y), t, (lx, ly) = state

        dirs = {"Up": (0, +1), "Down": (0, -1), "Left": (-1, 0), "Right": (+1, 0), "Pause": (0, 0)}

        for action_name, (dx, dy) in dirs.items():
            nx, ny = x + dx, y + dy
            nt = t + 1 if t != 5 else 1

            nlx, nly = lx, ly
            if nt == 2:
                nlx, nly = nx, ny

            new_state = ((nx, ny), nt, (nlx, nly))
            if self.check_valid(new_state):
                successors[action_name] = new_state

        return successors


read_two = lambda: tuple(map(int, input().split()))
if __name__ == '__main__':
    N, M = read_two()
    man_pos = read_two()
    target_pos = read_two()
    timer = int(input())
    laser_pos = read_two()
    allowed = [read_two() for _ in range(int(input()))]

    initial = (man_pos, timer, laser_pos)

    problem = Laser(initial, (N, M), target_pos, allowed)

    result = breadth_first_graph_search(problem)

    if result is not None:
        print(result.solution())
    else:
        print('No Solution!')


