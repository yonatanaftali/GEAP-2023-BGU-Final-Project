# The Genetic Maze Solver (GEAP-2023-BGU Final Project)

## Submitters

- Yonatan Naftali (313232829)
- Omer Popol (31496055)

## Introduction

A genetic algorithm is a type of optimization algorithm that is inspired by the process of natural selection. It is used
to find approximate solutions to optimization and search problems.

The basic idea behind a genetic algorithm is to start with a population of candidate solutions, and then repeatedly
apply a set of genetic operators (such as mutation, crossover, and selection) to the population in order to evolve the
solutions over time. The hope is that after many generations, the population will converge on an optimal or near-optimal
solution to the problem. Genetic algorithms have been applied to a wide range of problems, including function
optimization, scheduling, and machine learning.

Genetic algorithms can be used to optimize strategies for playing games by simulating the process of natural selection.
This can be done by creating a population of candidate solutions (in the form of game-playing agents or "players"), and
then repeatedly applying genetic operators such as mutation, crossover, and selection to evolve the population over
time. The goal is to evolve a population of players that are able to perform well in the game.

One way this can be achieved is by using a fitness function that assigns a score to each player based on their
performance in the game. The fitness function can take into account various factors such as the player's win-loss
record, the number of moves made, and the score. Players with better fitness scores are more likely to be selected to
reproduce and pass on their genetic information to the next generation. Over time, the population will evolve to have
players that are better at playing the game.

Genetic algorithms have been applied to a wide range of games, including chess, checkers, and Go. They have also been
used to optimize the strategies of game-playing AI agents in video games such as Super Mario Bros, and to improve the
performance of robotic agents in simulated environments.

There are several tools and libraries available that can be used to help with implementing and running genetic
algorithms. These tools typically provide a framework for implementing genetic algorithms, as well as built-in genetic
operators and selection methods.

EC-KitY is a tool that can be used to help with genetic algorithms, it is written in Python, currently it has
implemented Genetic Algorithm (GA) and tree-based Genetic Programming (GP), and it is
designed to support all popular EC paradigms (GA, GP, ES, convolution, multi-objective, etc). It is designed with modern
software engineering in mind, making it a comprehensive and efficient tool for running evolutionary algorithms.

We are using EC-KitY to implement our genetic algorithm.

We contributed our share by solving an [existing issue](https://github.com/EC-KitY/EC-KitY/issues/4) in the EC-Kity
repository with [this PR](https://github.com/EC-KitY/EC-KitY/pull/35).

## Problem Description

The problem we are trying to solve is **the maze problem**.

The problem of solving mazes can be seen as a search problem, where the goal is to find a path from a starting point to
a goal or exit point within a maze. The maze can be represented as a graph, with each cell or location in the maze being
a node, and the edges connecting the nodes representing the paths between the cells. The challenge is to find the most
efficient path through the maze while avoiding obstacles and dead ends.

One common approach to solving mazes is to use a search algorithm such as depth-first search or breadth-first search to
explore the maze and find the shortest path. These algorithms work by starting at the starting point and then
systematically exploring the neighboring nodes in the maze until the goal or exit point is found.

However, this can be challenging, particularly with more complex mazes that have many obstacles and dead ends.
Additionally, the mazes can have loops, which means that the search algorithms can get stuck in an infinite loop, making
it impossible to find the exit.

Another approach is to use a genetic algorithm to optimize a solution to the maze. This algorithm can be used to evolve
a population of candidate solutions, in the form of paths through the maze, and then repeatedly applying genetic
operators such as mutation, crossover, and selection to evolve the population over time. The goal is to evolve a
population of paths that are able to navigate the maze efficiently.

## Solution Description

In our project we will demonstrate how you can solve a maze using a genetic algorithm. In this section we will describe
the genetic algorithm we are using to solve the maze problem. Details of the implementation can be found in the Software
Overview section.

1. **Representing the maze:** The first step is to represent the maze in a way that it can be used by the genetic
   algorithm.
   We achieved this by using a matrix, where each location in the maze is represented as a node, and
   the edges connecting the nodes represent the paths between the cells. Some cells can be considered as blocked, and
   some can be considered as the starting point and the exit point. More on that later, in the Software Overview
   section. An example maze:
   ```
   [2, 0, 1, 1, 1, 1, 0, 1, 1, 1]
   [1, 1, 1, 0, 0, 1, 0, 0, 1, 0]
   [0, 0, 0, 1, 0, 1, 1, 1, 1, 0]
   [1, 1, 1, 1, 1, 0, 0, 0, 1, 1]
   [1, 0, 0, 1, 0, 1, 1, 1, 0, 1]
   [1, 1, 0, 1, 1, 1, 0, 0, 1, 1]
   [0, 1, 0, 1, 0, 1, 1, 0, 1, 0]
   [1, 1, 0, 1, 0, 1, 0, 1, 1, 1]
   [1, 0, 0, 1, 1, 0, 1, 1, 0, 1]
   [1, 1, 1, 0, 1, 1, 1, 0, 1, 3]
   ```
2. **Initial population:** The next step is to create an initial population of candidate solutions. These solutions are
   suggested paths through the maze, and generated randomly.
   A solution is represented as a string of numbers, where each number represents a direction to move in the maze. The
   size of the population and the length of the solution string is determined by the user, and it can be experimentally
   determined. The numbers are mapped to the following directions: 0 - up, 1 - right, 2 - down, 3 - left. An example
   candidate solution with length of 25:
   ```
   [1, 2, 1, 1, 0, 0, 1, 0, 1, 0, 2, 2, 1, 0, 0, 2, 0, 3, 1, 2, 0, 2, 0, 3, 2]
   ```
3. **Fitness function:** A fitness function is used to evaluate the quality of the candidate solutions. This function
   assigns a fitness score to each path based on how well it navigates the maze. The fitness function take into
   account various factors such as the length of the path, the number of blocked cells encountered, and the distance to
   the goal. The lower the fitness score, the better the path is:
    - A score of 0 means that the path solved the maze using all of its available moves.
    - A score lower of 0 means that the path solved the maze using fewer moves than the maximum number of moves
      available.
    - A score higher than 0 means that the path did not solve the maze.


4. **Selection:** In this step, the genetic algorithm selects the fittest paths to reproduce and pass on their genetic
   information to the next generation. Tournament selection is used to select the fittest individuals from the
   population for reproduction. A small number of individuals (the tournament size) are randomly selected from the
   population, and the one with the lowest fitness is chosen as a parent for the next generation. This process is
   repeated until the desired number of parents have been selected. Tournament selection is a good method to use in this
   use case as it allows for a balance between exploration and exploitation, by allowing the selection of less fit
   individuals with potentially beneficial genetic variations while still maintaining a strong selection pressure on the
   population.


5. **Crossover:** In this step, the genetic algorithm combines the genetic information of two paths to create new paths.
   The crossover is done by selecting two paths and swapping a single step randomly. Crossover contributes to the
   algorithm by combining the genetic information of two high-performing paths to create new paths that may be even
   better at navigating the maze. For example, if one parent has a path sequence that is particularly good at
   avoiding obstacles (walls and out of bounds), and another parent has a path sequence that is particularly good at
   finding the exit quickly, then their offspring will inherit the best of both worlds.


6. **Mutation:** In this step, the genetic algorithm introduces small changes to the genetic information of the paths.
   The mutation is done by randomly changing the direction of a step in a path. Mutation contributes to the
   algorithm by introducing diversity into the population and prevent the GA from getting stuck in a local optimum. By
   introducing random changes, the algorithm is able to explore different solutions and potentially find a better one.
   Additionally, mutation also helps to prevent the GA from getting stuck in a loop, where the same solutions are
   repeatedly generated.


7. Repeat steps 4-6 for a number of generations: The genetic algorithm continues to repeat the selection, crossover, and
   mutation steps for a number of generations, until the optimal or near-optimal solution is found.


8. **Termination:** The algorithm stops when a termination criterion is met, after a certain number of generations. If
   we'd only look for a solution, and not the shortest solution, we could add an early termination checker to terminate
   when reaching the optimal fitness - 0.


9. **Output:** The final output is the path that has the lowest fitness score and is considered to be the optimal or
   near-optimal solution.

**Note:** The exact values used in all of the above steps, such as the mutation rate, are documented in the
project [environment file](./.env).

## Software Overview

### Initial Configuration

We allow the user to control some important parameters of the algorithm, including:

- Maze size (rows and columns)
- Size of the population
- Number of generations
- Probability of mutation
- Arity of the mutation
- Max solution length
- Use strict mode (see Solution Evaluation & Fitness Function section)
- Invalid solution penalty
- Wall bump penalty

This is done by using an [environment file](./.env), which is a file that contains the parameters.
Default values based on our experimentation will be used if not provided in the environment file.

### Running The Project

After configuring the environment file, you'll need to install the project dependencies using `pip`:

```bash
pip install -r requirements.txt
```

Then, you can run the project using the following command:

```bash
python main.py
```

### Maze Representation

We created a random maze generator using the Depth First Search (DFS) algorithm. Our generator takes in four
parameters: n and m, as dimensions of the maze, and start and end, as coordinates of the starting and ending points of
the maze. The maze is then generated using the following steps:

1. Create a stack that will be used to create the maze.
2. Initialize the maze as a matrix of size n x m, where each cell is a wall with value 0.
3. Initialize the visited matrix as a matrix of size n x m, where each cell is a boolean value that indicates whether
   the cell has been visited or not.
4. Initialize the parent matrix as a matrix of size n x m, where each cell is a tuple that indicates the parent of the
   cell (i.e. the cell that was visited before the current cell).
5. Push the starting cell into the stack.
6. While the stack is not empty:
    1. Pop the top cell from the stack and mark is as visited.
    2. Decide if the cell can be marked as walkable:
        - If the cell is the starting cell, mark it as walkable and as the starting cell.
        - If marking the cell as walkable will create a cycle in the maze, mark it as a wall (0). It does this by
          checking
          if the adjacent cell is in the boundaries of the maze, is marked as a walkable position, and is not the
          previous cell in the depth-first search path. If all these conditions are met, it means that the current
          cell must not be marked as a walkable cell to avoid creating a cycle. The code checks the adjacent position in
          all four directions (up, down, left, and right) to ensure that no cycle can be created.
        - Otherwise, mark it as walkable (1).
    3. Randomly insert the unvisited neighbors of the cell into the stack. If any of these neighbors are the exit cell,
       insert it into the top of the stack so that it is visited first and won't be marked as a wall.
    4. Mark the starting cell with 2 and the exit cell with 3.

The resulting maze is a matrix of size n x m, where each cell is either a wall (0), a walkable position (1), the start (
2), or the exit (3). At this point, the maze is has a single solution path. The final step is to randomly break walls to
create multiple solution paths. This is done by randomly selecting a wall and breaking it at a random chance.

Finally, the maze array is returned, representing the generated random maze, as provided in an example above. In
addition, we convert the "binary" maze in a visual representation, as shown below:

Blue = Entrance, Red = Wall, White = Path, Black = Exit

![Visual Image Of Maze](images/visual-maze-1.png?raw=true "Visual Image Of Maze")

### EC-KitY Configuration

1. **Initialization**: We used the `GABitStringVectorCreator(length=MAX_SOLUTION_LENGTH, bounds=(0, 3))` method to
   create
   the initial population. This creator creates a population of strings in the length of `MAX_SOLUTION_LENGTH` with
   values between 0 and 3. The population size is determined by the `POPULATION_SIZE` parameter.

2. **Selection**: We used the `TournamentSelection(tournament_size=4)` method to select the fittest individuals from the
   population for reproduction. A small number of individuals (the tournament size) are randomly selected from the
   population, and the one with the lowest fitness is chosen as a parent for the next generation.

3. **Crossover**: We used the `VectorKPointsCrossover(k=1)` method to combine the genetic information of two paths to
   create
   new paths. The crossover is done by selecting two paths and swapping a single step randomly.

4. **Mutation**: We used the `IntVectorOnePointMutation(probability=MUTATION_RATE, arity=MUTATION_ARITY)` method to
   introduce small changes to the genetic information of the paths. The mutation is done by randomly changing the
   direction of a step in a path.

5. **Fitness**: We created our own fitness function, `MazeEvaluator` which is described in the next section.

6. **Termination**: We define max number of generations, determined by the `MAX_GENERATIONS`parameter. We didn't define
   a
   TerminationChecker (early termination mechanism) since the paths are generated randomly, and we are not only
   interested in a solution that reaches the exit, but we care for the shortest path as well. If we had used an early
   termination mechanism, we would have missed the shortest path.

7. **Statistics**: We used the `BestAverageWorstStatistics(output_stream=open(STATISTICS_FILE, 'w'))` method to collect
   statistics about the population, such as the average fitness, the best fitness, and the best individual. We exported
   the statistics to a file, and analyzed it.

### Solution Evaluation & Fitness Function

Given a path, the maze solver will determine if the path is valid or not. It does this by navigating the maze using the
path and checking if the path reaches the exit. If in any point the path goes out of bounds - it is invalidated and the
individual is severely penalized.

The player fitness is determined by the number of steps it takes to reach the exit. The lower the number of steps, the
lower (and better) the fitness. The closer the player is to the exit, the lower (and better) the fitness.

We included two modes of operation: strict and non-strict. In strict mode, if in any
point the path bumps into a wall, it is invalidated and the individual is severely penalized. In non-strict mode, the
path is not invalidated if it bumps into a wall, but it is gently penalized.

We defined an Enum class to represent the possible directions that a path can take:

    class Direction(Enum):
       UP = 0
       RIGHT = 1
       DOWN = 2
       LEFT = 3

For every step in the solution, given the current position of the player, we try to move it in the direction of the
step:

      direction = Directions(individual.cell_value(i))
      if direction == Directions.UP:
          new_position = self.move_up(current_position)
      elif direction == Directions.RIGHT:
          new_position = self.move_right(current_position)
      elif direction == Directions.DOWN:
          new_position = self.move_down(current_position)
      elif direction == Directions.LEFT:
          new_position = self.move_left(current_position)

Then we check if the new position is valid:

- If the new position is equal to the current position, it means that the player is trying to move in a direction
  that is not allowed (e.g. trying to move up when the player is already at the top of the maze). In this case, the
  path is invalid and the individual is severely penalized. The fitness score is set to the player current distance from
  the exit plus the invalid solution penalty.
- If the new position is a **wall**, it means that the player is trying to move into a wall. In this case, we check if
  strict mode is enabled:
    - If it is, the path is invalid and the individual is severely penalized. The fitness score is set to the player
      current distance from the exit plus the invalid solution penalty.
    - If strict mode is not enabled, we keep the player at the same place they have been before they tried to move, and
      we gently penalize their future fitness score by adding the wall bump penalty to it.
- If the new position is the **exit**, it means that the player has reached the exit. In this case, the fitness score is
  set to 0 (the current distance from exit) plus any accumulated penalties minus the remaining steps in the player path.
  We want to reward player paths that are shorter, so we subtract the remaining steps from the fitness score.
- If the new position is a **walkable** position, it means that the player has moved to a valid position. In this case,
  we update the current position of the player to the new position, and we continue to the next step in the path.

The distance from the exit is calculated by using the Euclidian distance from the current point of the player (i.e the
player coordinates in the matrix) to the exit coordinates. We found that this distance formulae give us the best
assessment to the relative location of the player the exit, without going into complicated calculations of traversal
inside the maze.

Thus, an individual's fitness score signifies how close it is to the exit, and how many steps it took to reach it. The
best individual is the one with the lowest fitness score (i.e. the one that is closest to the exit and took the least
steps to reach it), and we want to keep and evolve the best individuals.

### Output

The program output the following details to the console:

![Console Output](images/console-output.png?raw=true "Console Output")

In the middle of the output, under the print `debug: random seed` you can find the best individual's path, and its
fitness score.

In addition, the program outputs the following files to the [output](./output) directory:

- Maze image
- Statistics file
- Average fitness graph
- Best fitness graph

Every run is identified by a unique timestamp, and the output files are named accordingly.

## Results

The results of the experiment depend on the parameters that we set and the generated maze. We ran the experiment with
different parameters, below are the results of the experiment with the following parameters:

### Maze Size 5x5, Strict Mode, Population Size 50, Generations 30, Mutation Rate 0.1, Mutation Arity 1

![Maze Size 5x5, Strict Mode, Population Size 50, Generations 30, Mutation Rate 0.1, Mutation Arity 1 - Maze](images/results-1-maze.png?raw=true "Maze Size 5x5, Strict Mode, Population Size 50, Generations 30, Mutation Rate 0.1, Mutation Arity 1 - Maze")
![Maze Size 5x5, Strict Mode, Population Size 50, Generations 30, Mutation Rate 0.1, Mutation Arity 1 - Avg Fitness](images/results-1-avg_fitness.png?raw=true "Maze Size 5x5, Strict Mode, Population Size 50, Generations 30, Mutation Rate 0.1, Mutation Arity 1 - Avg Fitness")
![Maze Size 5x5, Strict Mode, Population Size 50, Generations 30, Mutation Rate 0.1, Mutation Arity 1 - Best Fitness](images/results-1-best_fitness.png?raw=true "Maze Size 5x5, Strict Mode, Population Size 50, Generations 30, Mutation Rate 0.1, Mutation Arity 1 - Best Fitness")

**Translated Solution:**
`[down, down, right, right, right, right, up, up, right, right, down, right, down, up, right, right, right, up, right, down, right, down, left, left, up]`

**Fitness:** -18 (max solution length: 25)

### Maze Size 7x7, Strict Mode, Population Size 50, Generations 30, Mutation Rate 0.2, Mutation Arity 2

![Maze Size 7x7, Strict Mode, Population Size 50, Generations 30, Mutation Rate 0.2, Mutation Arity 2 - Maze](images/results-2-maze.png?raw=true "Maze Size 7x7, Strict Mode, Population Size 50, Generations 30, Mutation Rate 0.2, Mutation Arity 2 - Maze")
![Maze Size 7x7, Strict Mode, Population Size 50, Generations 30, Mutation Rate 0.2, Mutation Arity 2 - Avg Fitness](images/results-2-avg_fitness.png?raw=true "Maze Size 7x7, Strict Mode, Population Size 50, Generations 30, Mutation Rate 0.2, Mutation Arity 2 - Avg Fitness")
![Maze Size 7x7, Strict Mode, Population Size 50, Generations 30, Mutation Rate 0.2, Mutation Arity 2 - Best Fitness](images/results-2-best_fitness.png?raw=true "Maze Size 7x7, Strict Mode, Population Size 50, Generations 30, Mutation Rate 0.2, Mutation Arity 2 - Best Fitness")

**Translated Solution:**
`[right, right, up, up, down, up, up, right, right, right, left, left, right, right, right, left, left, down, up, up, left, up, up, up, up, right, up, down, up, up, left, down, up, down, left, up, left, up, left, down, down, down, left, left, left, up, down, up, left]`

**Fitness:** -35 (max solution length: 49)

### Maze Size 10x10, Strict Mode, Population Size 500, Generations 200, Mutation Rate 0.2, Mutation Arity 5

![Maze Size 10x10, Strict Mode, Population Size 500, Generations 200, Mutation Rate 0.2, Mutation Arity 5 - Maze](images/results-3-maze.png?raw=true "Maze Size 10x10, Strict Mode, Population Size 500, Generations 200, Mutation Rate 0.2, Mutation Arity 5 - Maze")
![Maze Size 10x10, Strict Mode, Population Size 500, Generations 200, Mutation Rate 0.2, Mutation Arity 5 - Avg Fitness](images/results-3-avg_fitness.png?raw=true "Maze Size 10x10, Strict Mode, Population Size 500, Generations 200, Mutation Rate 0.2, Mutation Arity 5 - Avg Fitness")
![Maze Size 10x10, Strict Mode, Population Size 500, Generations 200, Mutation Rate 0.2, Mutation Arity 5 - Best Fitness](images/results-3-best_fitness.png?raw=true "Maze Size 10x10, Strict Mode, Population Size 500, Generations 200, Mutation Rate 0.2, Mutation Arity 5 - Best Fitness")

**Translated Solution:**
`[right, up, right, left, down, up, right, right, down, right, left, right, left, down, down, right, down, up, left, right, down, up, right, up, down, right, right, down, right, right, up, up, up, left, down, up, up, down, left, right, up, down, right, down, down, up, right, right, left, right, right, up, up, up, down, up, left, up, up, up, left, right, up, down, down, left, up, up, down, up, left, down, left, left, right, up, left, up, up, right, right, left, right, left, down, down, right, right, left, down, down, left, right, up, left, left, up, left, down, right]`

**Fitness:** -70 (max solution length: 100)

### Maze Size 12x12, Population Size 300, Generations 30, Mutation Rate 0.2, Mutation Arity 1

![Maze Size 12x12, Population Size 300, Generations 30, Mutation Rate 0.2, Mutation Arity 1 - Maze](images/results-4-maze.png?raw=true "Maze Size 12x12, Population Size 300, Generations 30, Mutation Rate 0.2, Mutation Arity 1 - Maze")
![Maze Size 12x12, Population Size 300, Generations 30, Mutation Rate 0.2, Mutation Arity 1 - Avg Fitness](images/results-4-avg_fitness.png?raw=true "Maze Size 12x12, Population Size 300, Generations 30, Mutation Rate 0.2, Mutation Arity 1 - Avg Fitness")
![Maze Size 12x12, Population Size 300, Generations 30, Mutation Rate 0.2, Mutation Arity 1 - Best Fitness](images/results-4-best_fitness.png?raw=true "Maze Size 12x12, Population Size 300, Generations 30, Mutation Rate 0.2, Mutation Arity 1 - Best Fitness")

**Translated Solution:**
`[up, up, up, down, right, down, left, up, right, down, left, up, right, right, down, up, left, right, up, down, up, up, left, up, up, right, up, down, up, down, left, right, right, down, right, right, right, right, down, right, right, up, up, up, up, right, up, right, right, up, left, right, right, right, up, down, down, down, up, right, down, down, right, up, up, right, down, right, up, left, right, down, up, up, left, right, right, down, left, down, up, right, up, left, down, right, up, right, down, down, up, left, right, right, right, up, up, right, down, down, right, up, up, down, left, left, right, right, right, up, down, left, down, right, down, up, up, up, left, down, left, left, left, down, up, right, right, left, down, up, left, left, left, up, down, up, right, left, right, up, down, up, up, left]`

**Fitness:** -89 (max solution length: 144)

### Maze Size 20x20, Population Size 500, Generations 30, Mutation Rate 0.2, Mutation Arity 2

In the following example we can see how more generations are needed to find a solution.

![Maze Size 20x20, Population Size 500, Generations 30, Mutation Rate 0.2, Mutation Arity 2 - Maze](images/results-5-maze.png?raw=true "Maze Size 20x20, Population Size 500, Generations 30, Mutation Rate 0.2, Mutation Arity 2 - Maze")
![Maze Size 20x20, Population Size 500, Generations 30, Mutation Rate 0.2, Mutation Arity 2 - Avg Fitness](images/results-5-avg_fitness.png?raw=true "Maze Size 20x20, Population Size 500, Generations 30, Mutation Rate 0.2, Mutation Arity 2 - Avg Fitness")
![Maze Size 20x20, Population Size 500, Generations 30, Mutation Rate 0.2, Mutation Arity 2 - Best Fitness](images/results-5-best_fitness.png?raw=true "Maze Size 20x20, Population Size 500, Generations 30, Mutation Rate 0.2, Mutation Arity 2 - Best Fitness")

### Maze Size 20x20, Population Size 500, Generations 100, Mutation Rate 0.2, Mutation Arity 2

![Maze Size 20x20, Population Size 500, Generations 100, Mutation Rate 0.2, Mutation Arity 2 - Maze](images/results-6-maze.png?raw=true "Maze Size 20x20, Population Size 500, Generations 100, Mutation Rate 0.2, Mutation Arity 2 - Maze")
![Maze Size 20x20, Population Size 500, Generations 100, Mutation Rate 0.2, Mutation Arity 2 - Avg Fitness](images/results-6-avg_fitness.png?raw=true "Maze Size 20x20, Population Size 500, Generations 100, Mutation Rate 0.2, Mutation Arity 2 - Avg Fitness")
![Maze Size 20x20, Population Size 500, Generations 100, Mutation Rate 0.2, Mutation Arity 2 - Best Fitness](images/results-6-best_fitness.png?raw=true "Maze Size 20x20, Population Size 500, Generations 100, Mutation Rate 0.2, Mutation Arity 2 - Best Fitness")

**Translated Solution:**
`[up, right, right, up, right, left, right, right, down, down, right, left, right, up, down, left, up, left, right, left, up, up, right, right, right, down, up, down, down, right, left, down, right, right, left, left, right, up, right, left, right, down, up, right, up, down, up, up, down, down, left, right, down, right, right, right, up, up, up, up, up, up, right, left, right, left, right, left, up, left, right, right, left, left, right, left, up, up, right, right, left, up, up, up, up, right, up, right, up, left, down, up, down, up, down, up, right, right, down, right, right, down, up, down, right, down, left, up, left, right, right, left, right, up, right, up, right, right, right, right, right, down, up, up, right, down, right, right, right, right, up, up, down, right, up, down, right, down, down, right, right, down, down, left, up, up, down, right, right, up, up, right, right, down, right, up, up, up, down, left, left, up, left, left, up, left, left, up, up, down, up, down, right, left, left, up, right, up, right, up, right, up, left, down, left, left, down, right, left, right, down, up, up, up, left, down, down, left, down, down, right, left, right, down, down, left, left, left, right, up, up, up, right, down, up, left, right, down, up, left, up, right, left, down, down, down, right, left, up, right, down, up, up, up, left, left, right, up, up, down, up, left, left, left, up, down, down, up, right, down, down, right, right, left, down, left, up, left, down, down, right, down, right, up, up, right, down, down, down, right, right, up, up, up, up, up, up, up, left, up, down, left, up, down, left, down, right, left, up, up, up, left, up, up, down, up, left, down, down, left, up, left, right, down, right, down, up, up, down, right, right, down, up, down, left, left, down, up, left, up, up, up, down, up, up, right, left, up, right, left, up, left, left, up, right, up, down, left, up, up, down, left, up, up, left, left, right, right, right, up, down, left, right, right, down, left, up, left, down, left, down, left, up, up, left, up, up, up, left, down, down, left, up, left, right, down, up, right, down, right, left, down, right, down, down, right, right, right, right, left, left, down, up, left, up, up, left, up, down, down]`

**Fitness:** -261 (max solution length: 400)

## Conclusions & Summary

### Strict Mode

After running the experiment numerous times, on multiple mazes, with different parameters, we found a pattern that made
us think about the necessity of strict mode. Take a look at the following maze:

![Why Strict Mode Is Needed Maze](images/why-strict-mode-is-needed-maze.png?raw=true "Why Strict Mode Is Needed Maze")

The best solution the algorithm provided for that maze
was: `[0, 0, 2, 0, 1, 0, 2, 1, 3, 1, 2, 0, 2, 1, 1, 2, 3, 3, 1, 3, 2, 1, 3, 1, 0, 1, 2, 0, 1, 0, 2, 1, 3, 1, 0, 3, 2, 2, 3, 3, 0, 1, 0, 1, 3, 1, 3, 1, 0]`
which translate
to: `[up, up, down, up, right, up, down, right, left, right, down, up, down, right, right, down, left, left, right, left, down, right, left, right, up, right, down, up, right, up, down, right, left, right, up, left, down, down, left, left, up, right, up, right, left, right, left, right, up]`
.

If we follow the first 15 steps of the solution, we will get to the position (4,5), very close to the exit. However, in
the next move the player will try to move down into a wall thus the solution will be invalidated and severely penalized.
Thus, it won't matter how close the solution was to the exit, since it tried to make an illegal move it won't evolve.

If we had allowed the player to try to move into a wall, and just penalize them for it, the solution would have evolved,
and we would have found a solution that is much closer to the exit. Since we take into account the remaining steps in
the player path when calculating the fitness score, we don't mind if a
player will waste some of their moves trying to move into a wall as long as they will not go out of the maze.

### Mutation Rate & Arity

We have found that the mutation rate and the arity of the mutation have a significant impact on the results. When using
strict mode, the higher the mutation rate and the arity, the better the results. When not using strict mode, we found
that also a lower mutation rate and arity can produce good results. We believe that this is because in strict mode the
algorithm is needs to compensate for the fact that it does not allow the player to move into walls, and thus it needs to
evolve more aggressively.

### Population Size & Generations

We have found that the bigger the maze is, the larger the population size and the number of generations need to be. This
is because given a larger maze there are much more possible random solutions, and thus the algorithm needs more time to
evolve a good solution. If we use a small population size and a small number of generations, the algorithm will not have
enough time to evolve a good solution and will get stuck in a local minimum. In most cases, larger population size was
more beneficial than a larger number of generations.

### Max Solution Length

The max solution length must be at least as long as the number of steps it takes to reach the exit. If it is smaller
than that, the algorithm will not be able to find a solution. If it is larger than that, the algorithm will waste time
trying to evolve solutions that are longer than the shortest solution.

However, since we don't have a predefined solution length, we can't know what is the best value for this parameter. We
have found that the best value for this parameter is the size of the maze. This is because the algorithm will try to
evolve solutions that are as long as the maze, and thus it will have enough time to find the shortest solution. We
reward the algorithm for finding a shorter solution, and penalize it for finding a longer solution, so through evolution
it will find the shortest solution.

## Future Work

We would like to address two issues in the future that we have found during the experiment:

- **Stuck At Start:** One of the most common issues that we have encountered was that all the randomly generated
  initial solutions were stuck at the start of the maze. Their first step was always to move out of bounds or into a
  wall. That caused them to be penalized heavily, and thus they were not able to evolve. We tried solving this issue by
  introducing the strict mode - and it indeed helped with the wall issue, but not with the out-of-bounds issue. We
  thought about these possible solutions:
    - Introduce a new type of move - `stay`. This move will not change the player position, but will still count as a
      move. This will expand the options of the player.
    - Introduce a new very rare mutation type in addition to the existing mutation type - First move mutation. This
      mutation will change the first move of the solution to a random move. This will allow the algorithm to evolve
      solutions that are stuck at the start of the maze.


- **Max Solution Length:** As mentioned above, this is not a predefined value, but rather a parameter that we set. We
  would like to find a way to calculate the best value for this parameter, so that we don't need to set it manually. We
  would need to collect data from numerous runs of this project, on various maze sizes, with ranging parameters, in the
  form of `<maze size, optimal solution length>` and then use it to calculate the best value for this parameter for the
  given maze size.

## References

- [Genetic Algorithms Lectures By Guy Katabi](https://www.youtube.com/watch?v=XPx-a6MVne8&list=PLJH-8wFfkIYSEdJBhi89nd10_fuFYZyXm)
- [Introduction to Evolutionary Computing Slides](http://www.evolutionarycomputation.org/slides/)
- [Genetic and Evolutionary Algorithms and Programming: General Introduction and Appl. to Game Playing By Moshe Sipper](https://drive.google.com/file/d/0B6G3tbmMcpR4WVBTeDhKa3NtQjg/view?resourcekey=0-zLNbQBpLQ7jC_HVVQGLrzA)
- [Choosing Representation, Mutation, and Crossover in Genetic Algorithms](https://ieeexplore.ieee.org/document/9942691;jsessionid=wkmw2tMh3bFJ65RJSWLsRbUJ5hZEfONyGVxfLXgVBSaNWoiJSc2x!1934193416)
- [EC-KitY Wiki](https://github.com/EC-KitY/EC-KitY/wiki)
- [EC-KitY API](https://api.eckity.org/)
