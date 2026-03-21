from constraint import *

problem = Problem(solver=BacktrackingSolver())


# Variables: positions on the grid, Domains: whether there is a rook (1) or no rook (0)
# Names: 0, 1, 2, 3, 4, 5, 6, 7
# Values: 0, 1, 2, 3, 4, 5, 6, 7
variables = list(range(8))
domain = list(range(8))

problem.addVariables(variables, domain)


# Constraints:
# We know there are exactly 8 rooks. Each of them are in a different row.
# Constraint 1: make sure they are all in a different column.
# def constraint_1(*vars):
#     return len(set(vars)) == 8

# problem.addConstraint(constraint_1, variables)

problem.addConstraint(AllDifferentConstraint(), variables)

print(problem.getSolution())