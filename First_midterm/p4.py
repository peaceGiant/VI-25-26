from constraint import *


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # READ INPUT
    M = int(input())
    trees = []
    for _ in range(M):
        pos = tuple(map(int, input().split()))
        trees.append(pos)

    Xs = list(map(int, input().split()))


    # DEFINE VARIABLES AND DOMAIN
    variables = [f'tent_{i}' for i in range(1, M + 1)]
    for i, var in enumerate(variables):
        (tx, ty) = trees[i]
        neighs_tree = [(tx + dx, ty + dy) for (dx, dy) in [(0, 1), (1, 0), (-1, 0), (0, -1)] \
                       if 0 <= tx + dx < 6 and 0 <= ty + dy < 6]
        domain = neighs_tree
        problem.addVariable(var, domain)


    # DEFINE CONSTRAINTS
    # Constraint 1. No tents overlap.
    problem.addConstraint(AllDifferentConstraint(), variables)

    # Constraint 2. Each column i must have X[i] number of tents.
    def constraint_2(*tents):
        counts = [0] * M

        for (x, _) in tents:
            counts[x] += 1

        for count, X in zip(counts, Xs):
            if count != X:
                return False

        return True

    problem.addConstraint(constraint_2, variables)


    solution = problem.getSolution()

    # PRINT SOLUTION
    for (x, y) in sorted(solution.values(), key=lambda x: x[1]):
        print(x, y)
