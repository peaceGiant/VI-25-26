from searching_framework.utils import Problem
from searching_framework.informed_search import astar_search



class Farmer(Problem):

    def __init__(self, initial, goal):
        super().__init__(initial=initial, goal=goal)

    def check_valid(self, state):
        f, w, g, c = state
        return (w != g or g == f) and (g != c or g == f)

    def successor(self, state):
        successors = {}

        f, w, g, c = state

        # Farmer goes across alone
        nstate = (not f, w, g, c)
        if self.check_valid(nstate):
            successors['Farmer moves on his own'] = nstate

        # Farmer takes the wolf across
        nstate = (not f, not w, g, c)
        if f == w and self.check_valid(nstate):
            successors['Farmer moves wolf across'] = nstate

        # Farmer takes the goat across
        nstate = (not f, w, not g, c)
        if f == g and self.check_valid(nstate):
            successors['Farmer moves goat across'] = nstate

        # Farmer takes the cabbage across
        nstate = (not f, w, g, not c)
        if f == c and self.check_valid(nstate):
            successors['Farmer moves cabbage across'] = nstate

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        state = node.state
        state = list(state)

        return state.count(False) // 2


if __name__ == '__main__':
    initial = (False, False, False, False,)
    goal = (True, True, True, True,)

    problem = Farmer(initial, goal)

    print(astar_search(problem).solution())