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

In our project we will demonstrate how you can solve a maze using a genetic algorithm.
Our solution involves the following steps:

1. Representing the maze: The first step is to represent the maze in a way that it can be used by the genetic algorithm.
   This can be done by using a matrix or a graph, where each cell or location in the maze is represented as a node, and
   the edges connecting the nodes represent the paths between the cells. Some cells can be considered as blocked, and
   some can be considered as the starting point and the exit point.

2. Initial population: The next step is to create an initial population of candidate solutions. These solutions can be
   represented as paths through the maze, and can be generated randomly. The size of the population is determined by the
   user, and it can be experimentally determined.

3. Fitness function: A fitness function is used to evaluate the quality of the candidate solutions. This function
   assigns a fitness score to each path based on how well it navigates the maze. The fitness function can take into
   account various factors such as the length of the path, the number of blocked cells encountered, and the distance to
   the goal.

4. Selection: In this step, the genetic algorithm selects the fittest paths to reproduce and pass on their genetic
   information to the next generation. Selection is based on the fitness scores assigned by the fitness function.

5. Crossover: In this step, the genetic algorithm combines the genetic information of two paths to create new paths.
   Crossover can be done by selecting two paths and swapping their parts randomly.

6. Mutation: In this step, the genetic algorithm introduces small changes to the genetic information of the paths. This
   can be done by randomly changing the direction of a path or by swapping two cells in the path.

7. Repeat steps 4-6 for a number of generations: The genetic algorithm continues to repeat the selection, crossover, and
   mutation steps for a number of generations, until the optimal or near-optimal solution is found.

8. Termination: The algorithm stops when a termination criterion is met. This can be a certain number of generations, or
   when the path reaches a certain level of fitness.

Output: The final output is the path that has the highest fitness score and is considered to be the optimal solution.

## Software Overview

### Maze Representation

We created a random maze generator using the Depth First Search (DFS) algorithm. Our generator takes in three
parameters: n and m, as dimensions of the maze, and start and end, as coordinates of the starting and ending points of
the maze.

The generator first initializes two 2D arrays, maze and visited, which will be used to keep track of the maze and the
positions that have been visited, respectively. A stack s is also initialized and the starting position is inserted into
it.

The generator then enters a while loop that continues as long as the stack is not empty. In each iteration of the loop,
the top position of the stack is removed and marked as visited. The generator then checks if any of the adjacent
positions are valid (i.e. within the boundaries of the maze and not already marked as a path) and if so, marks them as
walkable positions adds them to the stack, and marks the current position as their previous position on the path. This
process is repeated until the stack is empty.

Additionally, the generator checks for cycles by comparing the previous position in the path with the current position,
and if it's the same, it will continue the loop without marking it.

Walls values are set to 0, walkable positions are set to 1, and the starting and ending positions are set to 2 and 3.

Finally, the maze array is returned, representing the generated random maze.

### Maze Solver

## Results

### Strict: True, Generations: 500:

![Strict: True, Generations: 500](results/result-1.png?raw=true "Strict: True, Generations: 500")

### Strict: True, Generations: 1000:

![Strict: True, Generations: 500](results/result-2.png?raw=true "Strict: True, Generations: 500")

### Strict: False, Generations: 200:

![Strict: True, Generations: 500](results/result-3.png?raw=true "Strict: True, Generations: 500")

## Summary

## References

- [Genetic Algorithms Lectures By Guy Katabi](https://www.youtube.com/watch?v=XPx-a6MVne8&list=PLJH-8wFfkIYSEdJBhi89nd10_fuFYZyXm)
- [Introduction to Evolutionary Computing Slides](http://www.evolutionarycomputation.org/slides/)
- [Genetic and Evolutionary Algorithms and Programming: General Introduction and Appl. to Game Playing By Moshe Sipper](https://drive.google.com/file/d/0B6G3tbmMcpR4WVBTeDhKa3NtQjg/view?resourcekey=0-zLNbQBpLQ7jC_HVVQGLrzA)
- [Choosing Representation, Mutation, and Crossover in Genetic Algorithms](https://ieeexplore.ieee.org/document/9942691;jsessionid=wkmw2tMh3bFJ65RJSWLsRbUJ5hZEfONyGVxfLXgVBSaNWoiJSc2x!1934193416)
- [EC-KitY Wiki](https://github.com/EC-KitY/EC-KitY/wiki)
- [EC-KitY API](https://api.eckity.org/)
