from constraint import *

problem = Problem(solver=BacktrackingSolver())



# Variables and Domain
problem.addVariable(1, [1, 2, 3, 4])  # V1: name=1, value in [1, 2, 3, 4]
problem.addVariable(2, [2, 3, 4])


# Constraints
problem.addConstraint(lambda x, y: x != y, [1, 2])



print(problem.getSolution())





