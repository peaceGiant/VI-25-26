import pygad
import numpy as np


def fitness_func(ga_instance, solution, solution_idx):
    ...


if __name__ == '__main__':
    ... # TODO: Read input


    params = {
            'num_generations': 300,
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