from constraint import *

problem = Problem(solver=BacktrackingSolver())

M = int(input())
trees = [tuple(map(int, input().split())) for _ in range(M)]

# Variables: we are going to have M variables, the positions of the trees
# Vi - interpret it as, the position of the tent i.
variables = []
for i, tree in enumerate(trees):
    var_name = tree
    dirs_ = {
        'up': (0, 1),
        'right': (1, 0),
        'down': (0, -1),
        'left': (-1, 0)
    }
    tx, ty = tree
    var_domain = [(tx + dx, ty + dy) for dx, dy in dirs_.values() if 0 <= tx + dx < 6 \
                  and 0 <= ty + dy < 6 \
                  and (tx + dx, ty + dy) not in trees]
    problem.addVariable(var_name, var_domain)
    variables.append(var_name)

# Constraints:
# They must be different
problem.addConstraint(AllDifferentConstraint(), variables)

# Tents mustn't be adjacent to each other (even diagonally)
def check_non_adjacency(t1, t2):
    t1x, t1y = t1
    t2x, t2y = t2
    return not (abs(t1x - t2x) <= 1 and abs(t1y - t2y) <= 1)

for i, var1 in enumerate(variables):
    for j, var2 in enumerate(variables[i:]):
        if i == j:
            continue
        problem.addConstraint(check_non_adjacency, [var1, var2])


res = problem.getSolution()
for tent in res.values():
    x, y = tent
    print(f'{x} {y}')












