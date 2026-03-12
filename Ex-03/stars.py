from searching_framework.utils import Problem
from searching_framework.uninformed_search import breadth_first_graph_search

class Stars_Problem(Problem):

    def __init__(self, initial, stars):
        super().__init__(initial)
        self.n = 8
        self.stars = stars

    def goal_test(self, state):
        k, b, s1, s2, s3 = state
        return all([s1, s2, s3])

    def check_valid(self, k):
        kx, ky = k
        return 0 <= kx < self.n and 0 <= ky < self.n

    def successor(self, state):
        kx, ky = state[0]
        bx, by = state[1]
        s1, s2, s3 = state[2], state[3], state[4]

        successors = {}

        # Actions: where the knight moves
        dirs = [(-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1)]
        actions = [f'K{i + 1}' for i in range(8)]

        for (dx, dy), action in zip(dirs, actions):
            nkx, nky = kx + dx, ky + dy
            ns1, ns2, ns3 = s1, s2, s3
            if (nkx, nky) in self.stars:
                ind_ = list(self.stars).index((nkx, nky))
                if ind_ == 0: ns1 = True
                if ind_ == 1: ns2 = True
                if ind_ == 2: ns3 = True
            if self.check_valid((nkx, nky)):
                successors[action] = ((nkx, nky), (bx, by), ns1, ns2, ns3)

        # Actions: where the bishop moves
        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        actions = [f'B{i + 1}' for i in range(4)]

        for (dx, dy), action in zip(dirs, actions):
            nbx, nby = bx + dx, by + dy
            ns1, ns2, ns3 = s1, s2, s3
            if (nbx, nby) in self.stars:
                ind_ = list(self.stars).index((nbx, nby))
                if ind_ == 0: ns1 = True
                if ind_ == 1: ns2 = True
                if ind_ == 2: ns3 = True
            if self.check_valid((nbx, nby)):
                successors[action] = ((kx, ky), (nbx, nby), ns1, ns2, ns3)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]



if __name__ == '__main__':
    knight = (2, 5)
    bishop = (5, 1)
    stars = ((1, 1), (4, 3), (6, 6))
    s1, s2, s3 = False, False, False

    initial = (knight, bishop, s1, s2, s3)
    problem = Stars_Problem(initial, stars)

    print(breadth_first_graph_search(problem).solution())
