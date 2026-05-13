
## 1. Maximize crop coverage with sprinklers

A farmer needs to place sprinklers on his farm to water his crops.

The plot of land is an $M \times N$ grid. The plot consists of crops which can be watered, and tiles which are blocked/unusable. The number of unusable tiles, and the positions of the tiles themselves are provided in the input at the very end.  

The farmer has $K$ sprinklers. Any number of sprinklers up to $K$ can be placed on the grid, and sprinklers can be placed on any tile. If a sprinkler is placed on a crop tile, the crops must be destroyed. A sprinkler waters all nearby tiles in a rhomb shape (♦), i.e. it waters all 8 adjacent tiles, as well as the 4 tiles which are at a distance 2 to the left, above, right or below the sprinkler.

Using a genetic algorithm, maximize the number of watered crops.
If multiple solutions water the same number of crops, the solution that uses fewer sprinklers should be preferred.

Print the number of watered crops, as well as the number of used sprinklers and their positions.

### Starter code

```python
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
    
```

### Example test cases

```python
5 5
2
3
1 1
2 2
4 0
```

```python
15 20
8
25
0 3
0 7
1 5
1 12
2 2
2 18
3 9
4 4
4 15
5 1
5 10
6 6
6 17
7 8
7 13
8 0
8 19
9 5
10 11
11 3
11 16
12 7
13 14
14 2
14 18
```


## 1.1 Chess maximal coverage

An extension of the previous problem, for those who want a challenge.

Use GA to maximize the coverage of six chess pieces (Pawn, Knight, Bishop, Rook, Queen, King). See: https://hexpiece.com/


## 2. Factory maintenance

A factory must schedule maintenance tasks for its machines using repair teams.

The factory contains $N$ machines. Each machine has a repair duration $t_i$ and a machine type $c_i$. The information for all machines is provided in the input.

Machines are partitioned into teams of exactly 4 machines. Every machine must belong to exactly one team.

Normally, the duration of a team shift is equal to the maximum repair duration among the 4 assigned machines.

However, before maintenance begins, the factory management selects one preferred machine type $P$. If all 4 machines assigned to a team are of the preferred type $P$, the technicians can efficiently reuse tools and calibration settings, and the duration of that team becomes the minimum repair duration among the 4 machines instead. All other teams still use the normal rule (maximum repair duration).

Using a genetic algorithm, determine how to partition the machines into teams of 4 and choose which machine type should be selected as the preferred type so that the total maintenance time of all teams is minimized.

Print the minimum total maintenance time, the selected preferred machine type and the teams and the machines assigned to each team.


## Starter code
```python
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
```


## Example test cases

```python
12
10 A
12 A
8 A
9 A
15 B
6 B
11 B
7 B
14 C
13 C
5 C
9 C
```

```python
24
10 A
12 A
8 A
9 A
15 A
7 A
11 A
13 A
20 B
18 B
17 B
16 B
21 B
19 B
14 B
15 B
5 C
6 C
7 C
8 C
9 D
10 D
11 D
12 D
```


## 3. Optimizing parameters of models

In this task, you need to use a Genetic Algorithm implemented with the `pygad` library in order to optimize the hyperparameters of a `DecisionTreeClassifier`.

The dataset given in the starting code is represented as a list of lists, where the class label is stored at last position of each row. The dataset should be split into training and testing subsets such that **the first 75% of the data** is in the **training set**, while the rest are in the testing set.

The Genetic Algorithm should optimize the following hyperparameters with their respective candidate values:

- `criterion: 'gini', 'entropy'`
- `max_depth: 5, 10, 15, 20, 25`
- `min_samples_split: 2, 3, 4, 5, 10`
- `max_leaf_nodes: 5, 10, 15, 20, 25`

The fitness function should primarily maximize classification accuracy on the test set. However, when two models achieve similar accuracy, smaller trees should be preferred. For this reason, the fitness function should slightly penalize larger values of `max_depth` and `max_leaf_nodes.`

Complete the missing parts of the starter code. After the Genetic Algorithm finishes, retrieve the best solution and print the *best* parameters for the decision tree. 

After that, create the *best* decision tree model, train it, and print its final accuracy on the test set.

### Starter code
```python
import pygad  
from sklearn.tree import DecisionTreeClassifier  
  
  
dataset = [  
    [2, 3, 1, 7, 0],  
    [5, 6, 4, 3, 1],  
    [1, 1, 2, 8, 1],  
    [7, 8, 6, 4, 1],  
    [3, 2, 1, 9, 0],  
    [8, 7, 5, 2, 1],  
    [4, 5, 2, 6, 1],  
    [1, 3, 1, 9, 0],  
    [9, 8, 7, 2, 1],  
    [2, 2, 3, 8, 0],  
    [6, 5, 4, 3, 1],  
    [1, 0, 2, 9, 0],  
    [7, 7, 6, 5, 1],  
    [2, 1, 1, 8, 0],  
    [8, 9, 5, 3, 1],  
    [3, 4, 2, 7, 0],  
    [5, 5, 5, 4, 0],  
    [0, 1, 1, 9, 0],  
    [9, 9, 8, 1, 1],  
    [2, 3, 2, 7, 0],  
    [6, 7, 5, 3, 1],  
    [1, 2, 0, 8, 0],  
    [8, 6, 7, 2, 0],  
    [3, 1, 2, 9, 0],  
    [7, 5, 6, 4, 1],  
    [2, 0, 1, 8, 0],  
    [9, 7, 8, 2, 1],  
    [4, 3, 2, 7, 0],  
    [6, 6, 5, 4, 1],  
    [1, 1, 0, 9, 0],  
    [8, 8, 6, 3, 1],  
    [2, 2, 1, 8, 0],  
    [7, 9, 5, 2, 1],  
    [3, 2, 2, 7, 0],  
    [5, 7, 4, 3, 1],  
    [0, 1, 2, 9, 0],  
    [9, 8, 6, 2, 0],  
    [2, 3, 1, 8, 0],  
    [6, 5, 5, 4, 1],  
    [1, 0, 1, 9, 0],  
    [8, 7, 7, 2, 1],  
    [3, 1, 1, 8, 0],  
    [7, 6, 5, 3, 0],  
    [2, 2, 0, 9, 0],  
    [9, 9, 7, 1, 1],  
    [4, 2, 2, 7, 0],  
    [6, 8, 5, 2, 1],  
    [1, 1, 1, 8, 1],  
    [8, 6, 6, 3, 1],  
    [2, 0, 2, 9, 1],  
    [7, 7, 5, 4, 1],  
    [3, 2, 1, 8, 0],  
    [9, 8, 8, 2, 1],  
    [1, 0, 0, 9, 0],  
    [6, 6, 4, 3, 1],  
    [2, 1, 2, 8, 0],  
    [8, 9, 6, 2, 1],  
    [4, 3, 1, 7, 0],  
    [7, 5, 5, 4, 1],  
    [1, 2, 1, 9, 0],  
    [9, 7, 6, 1, 1],  
    [2, 2, 2, 8, 0],  
    [6, 8, 7, 3, 1],  
    [0, 1, 1, 8, 0],  
    [8, 8, 5, 2, 1],  
    [3, 2, 0, 9, 0],  
    [7, 6, 6, 4, 1],  
    [1, 1, 2, 8, 0],  
    [9, 9, 5, 1, 1],  
    [2, 3, 0, 9, 0],  
    [6, 7, 6, 3, 1],  
    [1, 0, 1, 8, 0],  
    [8, 7, 5, 3, 1],  
    [3, 1, 0, 9, 0],  
    [7, 8, 7, 2, 1],  
    [2, 2, 1, 9, 0],  
    [9, 6, 8, 1, 1],  
    [4, 2, 1, 8, 0],  
    [6, 5, 6, 4, 1],  
    [1, 1, 0, 8, 0]  
]  
  
... # TODO: Split dataset here  
  
  
def fitness_func(ga_instance, solution, solution_idx):  
    ...  # TODO: Define fitness function  
  
  
ga_instance = pygad.GA(  
    num_generations=40,  
    sol_per_pop=50,  
    num_parents_mating=25,  
    fitness_func=fitness_func,  
    num_genes=...,  # TODO: Define missing params  
    gene_space=...,  
    mutation_num_genes=1  
)  
  
ga_instance.run()  
best_solution, _, _ = ga_instance.best_solution()  
  
...  # TODO: Print best params and accuracy of best model
```

