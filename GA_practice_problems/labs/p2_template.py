import pygad


N = int(input())
E = int(input())

dist = [list(map(float, input().split())) for _ in range(N)]


def decode(solution):
    ...


def fitness_func(ga, solution, idx):
    ...


gene_space = []


params = {
    'num_generations': 500,
    'sol_per_pop': 100,
    'num_parents_mating': 50,

    'num_genes': ...,
    'gene_space': gene_space,

    'fitness_func': fitness_func,

    'mutation_num_genes': 1,
    'save_best_solutions': True
}


ga = pygad.GA(**params)

ga.run()

solution, _, _ = ga.best_solution()
fitness = fitness_func(None, solution, 0)
best_solutions = ga.best_solutions

route1, route2 = decode(solution)

print("Friend 1 route:", route1)
print("Friend 2 route:", route2)
print("Fitness:", fitness)

# submit_data(fitness_func, decode, best_solutions)
