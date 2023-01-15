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
designed to support all popular EC paradigms (GA, GP, ES, coevolution, multi-objective, etc). It is designed with modern
software engineering in mind, making it a comprehensive and efficient tool for running evolutionary algorithms.

We are using EC-KitY to implement our genetic algorithm.

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

8. **Termination:** The algorithm stops when a termination criterion is met. This can be a certain number ofz
   generations, or when a suggested solution path reaches a certain level of fitness.

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
- Use strict mode (wall bump = invalid solution)
- Invalid solution penalty
- Wall bump penalty

This is done by using an [environment file](./.env), which is a file that contains the parameters.
Default values based on our experimentation will be used if not provided in the environment file.

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

Thus, an individual's fitness score signifies how close it is to the exit, and how many steps it took to reach it. The
best individual is the one with the lowest fitness score (i.e. the one that is closest to the exit and took the least
steps to reach it), and we want to keep and evolve the best individuals.

## Results

### Strict: True, Generations: 500

![Strict: True, Generations: 500](images/result-1.png?raw=true "Strict: True, Generations: 500")

### Strict: True, Generations: 1000

![Strict: True, Generations: 500](images/result-2.png?raw=true "Strict: True, Generations: 500")

### Strict: False, Generations: 200

![Strict: True, Generations: 500](images/result-3.png?raw=true "Strict: True, Generations: 500")

## Summary

## References

- [Genetic Algorithms Lectures By Guy Katabi](https://www.youtube.com/watch?v=XPx-a6MVne8&list=PLJH-8wFfkIYSEdJBhi89nd10_fuFYZyXm)
- [Introduction to Evolutionary Computing Slides](http://www.evolutionarycomputation.org/slides/)
- [Genetic and Evolutionary Algorithms and Programming: General Introduction and Appl. to Game Playing By Moshe Sipper](https://drive.google.com/file/d/0B6G3tbmMcpR4WVBTeDhKa3NtQjg/view?resourcekey=0-zLNbQBpLQ7jC_HVVQGLrzA)
- [Choosing Representation, Mutation, and Crossover in Genetic Algorithms](https://ieeexplore.ieee.org/document/9942691;jsessionid=wkmw2tMh3bFJ65RJSWLsRbUJ5hZEfONyGVxfLXgVBSaNWoiJSc2x!1934193416)
- [EC-KitY Wiki](https://github.com/EC-KitY/EC-KitY/wiki)
- [EC-KitY API](https://api.eckity.org/)
