from searching_framework import *

class Boxes(Problem):
    def __init__(self, initial, n, boxes):
        super().__init__(initial)
        self.n = n
        self.boxes = boxes

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        boxes = state[1]
        return len(boxes) == 0

    def check_valid(self, state):
        (x, y), boxes = state
        if not (0 <= x < self.n and 0 <= y < self.n):
            return False

        if (x, y) in self.boxes:
            return False

        return True

    def h1(self, node):
        state = node.state
        num_boxes = len(state[1])
        return num_boxes / 3

    def md(self, man, box):
        mx, my = man
        bx, by = box
        return abs(mx - bx) + abs(my - by)

    def h(self, node):
        state = node.state
        man = state[0]
        boxes = state[1]
        dists = []

        for (bx, by) in boxes:
            neigb_cells = [(bx + dx, by + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] \
             if 0 <= bx + dx < self.n and 0 <= by + dy < self.n]
            min_dist = min(list(map(lambda x: self.md(man, x), neigb_cells)))
            dists.append(min_dist)

        return max(dists) if len(dists) >= 1 else 0

    def h3(self, node):
        state = node.state
        man = state[0]
        boxes = state[1]

        dists_ = []
        for box in boxes:
            dists_.append(self.md(man, box) - 2)

        # return max(dists_) if max(dists_) > 0 else 0
        return min(dists_) if min(dists_) > 0 else 0

    def successor(self, state):
        successors = {}

        (x, y), boxes = state

        # Man goes down
        nx, ny = x, y - 1
        nboxes = []

        # Is the player near a box?
        for (bx, by) in boxes:
            if abs(nx - bx) <= 1 and abs(ny - by) <= 1:
                pass
            else:
                nboxes.append((bx, by))

        new_state = ((nx, ny), tuple(nboxes))

        if self.check_valid(new_state):
            successors['down'] = new_state

        # Man goes left
        nx, ny = x - 1, y
        nboxes = []

        # Is the player near a box?
        for (bx, by) in boxes:
            if abs(nx - bx) <= 1 and abs(ny - by) <= 1:
                pass
            else:
                nboxes.append((bx, by))

        new_state = ((nx, ny), tuple(nboxes))

        if self.check_valid(new_state):
            successors['left'] = new_state

        return successors


if __name__ == '__main__':
    n = int(input())
    man_pos = (n-1, n-1)

    num_boxes = int(input())
    boxes = list()
    for _ in range(num_boxes):
        boxes.append(tuple(map(int, input().split(','))))

    initial = (man_pos, tuple(boxes))

    problem = Boxes(initial, n, boxes)

    result = breadth_first_graph_search(problem)

    if result is not None:
        print(result.solution())
    else:
        print('No Solution!')

    result = astar_search(problem)

    if result is not None:
        print(result.solution())
    else:
        print('No Solution!')
