from constraint import *

problem = Problem(solver=BacktrackingSolver())

# Variables and Domains
variables = list(range(1, 17))  # [1, 2, ..., 16]
domain = list(range(1, 17))

problem.addVariables(variables, domain)

# Constraints
# Constraint 1: Each row must sum to 34
for i in range(4):
    row_vars = [1 + i * 4, 2 + i * 4, 3 + i * 4, 4 + i * 4]
    problem.addConstraint(ExactSumConstraint(34), row_vars)

# Constraint 2: Each column must sum to 34
for i in range(4):
    col_vars = [1 + i, 5 + i, 9 + i, 13 + i]
    problem.addConstraint(ExactSumConstraint(34), col_vars)

# Constraint 3: Diagonals must sum to 34
main_diag = [1, 6, 11, 16]
alt_diag  = [4, 7, 10, 13]

problem.addConstraint(ExactSumConstraint(34), main_diag)
problem.addConstraint(ExactSumConstraint(34), alt_diag)

# Constraint 4: All values must be different
problem.addConstraint(AllDifferentConstraint(), variables)

print(problem.getSolution())







