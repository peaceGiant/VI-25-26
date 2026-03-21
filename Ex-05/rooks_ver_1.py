from constraint import *

problem = Problem(solver=BacktrackingSolver())


# Variables: positions on the grid, Domains: whether there is a rook (1) or no rook (0)
# Names: (0, 0), (0, 1), ...
# Values: [0, 1]
variables = []
domain = [0, 1]

for i in range(8):
    for j in range(8):
        problem.addVariable((i, j), domain)
        variables.append((i, j))


# Constraints:
# Make sure there are 8 rooks on the grid
def constraint_1(*vars):  # * helps with combining the 64 inputs into a singular list vars
    counter = 0
    for cell in vars:
        if cell == 1:
            counter += 1

    return counter == 8

# Each row must have a singular rook. This constraint checks one row/column.
def constraint_2(*vars):
    counter = 0
    for cell in vars:
        if cell == 1:
            counter += 1

    return counter == 1

problem.addConstraint(constraint_1, variables)  # constraint_1(x1, x2, ..., x64) vars=[x1, x2, ..., x64]
for i in range(8):
    row = [(i, j) for j in range(8)]
    column = [(j, i) for j in range(8)]
    problem.addConstraint(constraint_2, row)
    problem.addConstraint(constraint_2, column)


print(problem.getSolution())