import pygad
import random
random.seed(0)

rooms = {
    1: {'name': 'Modern & Contemporary Art', 'adjacent': [2, 7], 'value': 110},
    2: {'name': 'European History', 'adjacent': [1, 3, 4, 5, 7], 'value': 130},
    3: {'name': 'Seasonal Exhibitions', 'adjacent': [2], 'value': 100},
    4: {'name': 'Prehistory', 'adjacent': [2, 6, 10], 'value': 140},
    5: {'name': 'Medieval Times', 'adjacent': [2, 6, 9], 'value': 120},
    6: {'name': 'Arms and Armor', 'adjacent': [4, 5], 'value': 150},
    7: {'name': 'Arts of Africa, Oceania and the Americas', 'adjacent': [1, 2, 8], 'value': 90},
    8: {'name': 'Greek and Roman History', 'adjacent': [7, 9], 'value': 180},
    9: {'name': 'The Great Hall', 'adjacent': [5, 8, 10], 'value': 30},
    10: {'name': 'Egyptian History', 'adjacent': [4, 9], 'value': 200}
}
large_rooms = [2, 8, 9, 10]

K = int(input())


def decode(solution):
    counts = [0] * len(rooms)

    for room in solution:
        room = int(room)
        room_idx = room - 1

        if room not in large_rooms:
            counts[room_idx] = 1
        else:
            counts[room_idx] = min(2, counts[room_idx] + 1)

    return counts


def fitness_func(ga, solution, idx):
    counts = decode(solution)

    coverage = [0] * len(rooms)

    for i, count in enumerate(counts):
        if count == 0:
            continue

        room_num = i + 1

        # Protected value of room itself
        if room_num not in large_rooms:  # small room
            coverage[i] = 100
        else:  # Large room
            if count == 1:
                coverage[i] += 60
                coverage[i] = min(100, coverage[i])
            else:
                coverage[i] = 100

        adjs = rooms[room_num]['adjacent']

        # Protected value of adjacent rooms
        for adj in adjs:
            adj_idx = adj - 1
            coverage[adj_idx] += 10 * count  # IMPORTANT: each functional camera adds 10% coverage
            coverage[adj_idx] = min(100, coverage[adj_idx])

    # Calculation of fitness
    fitness = 0

    for i, c in enumerate(coverage):
        room_num = i + 1
        value = rooms[room_num]['value']
        fitness += value * c / 100

    return fitness


params = {
    'num_generations': 1000,
    'sol_per_pop': 100,
    'num_parents_mating': 40,

    'num_genes': K,
    'gene_space': list(range(1, len(rooms) + 1)),

    'fitness_func': fitness_func,

    'mutation_num_genes': 1
}

ga = pygad.GA(**params)

ga.run()

best_solution, _, _ = ga.best_solution()
best_fitness = fitness_func(None, best_solution, 0)

print(f'Optimal protected value: {best_fitness}M$')
# print(best_solution)
