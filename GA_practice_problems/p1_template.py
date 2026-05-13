import pygad


def read_input():
    M, N = map(int, input().split())
    K = int(input())
    B = int(input())

    unusable = set()
    for _ in range(B):
        r, c = map(int, input().split())
        unusable.add((r, c))

    return M, N, K, unusable


def fitness_func(ga_instance, solution, solution_idx):
    ...  # TODO: implement fitness function


if __name__ == "__main__":
    M, N, K, unusable = read_input()

    params = {
        'num_generations': 100,
        'sol_per_pop': 50,
        'num_parents_mating': 20,
        'num_genes': ...,  # TODO: fill empty params
        'gene_space': ...,
        'fitness_func': fitness_func,
        'mutation_num_genes': 1
    }

    ga = pygad.GA(**params)
    ga.run()

    best_solution, _, _ = ga.best_solution()

    ...  # TODO: Print required data
