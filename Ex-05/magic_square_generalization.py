# A more advanced version. Just for those who are curious.
from constraint import *

problem = Problem(solver=BacktrackingSolver())

n = int(input())

# Variables and Domains
variables = list(range(1, (n ** 2) + 1))  # [1, 2, ..., n^2]
domain = list(range(1, (n ** 2) + 1))

problem.addVariables(variables, domain)

def get_val_at_pos(x, y):
    """Return the 1-indexed value of the tile for 0-indexed (x, y)."""
    return (y + 1) + x * n

# Constraints
# Constraint 1: All values must be different
problem.addConstraint(AllDifferentConstraint(), variables)
# We put this constraint first since it is powerful, prunes a lot of options early.

# Constraint 2: Each row must sum to x. Sum of the entire grid is n * x.
# But on the other hand, sum of the entire grid is 1 + 2 + ... + n^2 = n^2 * (n^2 + 1) / 2.
# We have n * x = n^2 * (n^2 + 1) / 2   =>  x = n * (n^2 + 1) / 2
x = n * (n ** 2 + 1) // 2
for i in range(n):
    row_vars = [get_val_at_pos(i, j) for j in range(n)]
    problem.addConstraint(ExactSumConstraint(x), row_vars)

# Constraint 3: Each column must sum to x
for i in range(n):
    col_vars = [get_val_at_pos(j, i) for j in range(n)]
    problem.addConstraint(ExactSumConstraint(x), col_vars)

# Constraint 4: Diagonals must sum to x
main_diag = [get_val_at_pos(i, i) for i in range(n)]
alt_diag  = [get_val_at_pos(i, n - 1 - i) for i in range(n)]

problem.addConstraint(ExactSumConstraint(x), main_diag)
problem.addConstraint(ExactSumConstraint(x), alt_diag)


print(problem.getSolution())

