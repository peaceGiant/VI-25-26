import pygad

N, M, R = map(float, input().split())
N = int(N)
M = int(M)

points = [tuple(map(float, input().split())) for _ in range(N)]

# Part 1.
def decode(solution):
    ...


def fitness_func(ga, solution, idx):
    ...


gene_space = [{'low': R, 'high': 5-R}, {'low': R, 'high': 10-R}, [0, 1]] * N


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

print(solution)
print(fitness)


# Part 2.
chromosomes = [...]


# submit_data(fitness_func, decode, chromosomes, best_solutions)