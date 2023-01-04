import random
from enum import Enum
from typing import List
from math import sqrt

import numpy as np

from eckity.evaluators.simple_individual_evaluator import SimpleIndividualEvaluator

from maze_generator import random_maze_generator

# Should we the maze size -> n*m
MAX_SOLUTION_LENGTH = 100


class Directions(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class MazeEvaluator(SimpleIndividualEvaluator):
    """
    Evaluator class for the Maze problem, responsible for defining a fitness evaluation method and evaluating it.
    Fitness is the distance to the exit

    Attributes
    -------
    maze: List[List[int]]
        The maze to be solved
    n: int
        The number of rows in the maze
    m: int
        The number of columns in the maze
    """

    def __init__(self, n=10, m=10):
        super().__init__()

        # Generate a random maze for the problem
        self.start = (random.randint(0, n - 1), 0)
        self.end = (random.randint(0, n - 1), m - 1)
        self.n = n
        self.m = m
        self.maze = random_maze_generator(self.n, self.m, self.start, self.end)

    def _evaluate_individual(self, individual):
        """
        Compute the fitness value of a given individual.

        Parameters
        ----------
        individual: Vector
            The individual to compute the fitness value for.

        Returns
        -------
        float
            The evaluated fitness value of the given individual.

            0 fitness = solved
            > 0 fitness = distance to the exit
            np.inf fitness = invalid solution

        """

        current_position = self.start
        new_position = current_position
        for i in range(individual.size()):
            direction = Directions(individual.cell_value(i))
            if direction == Directions.UP:
                new_position = self.move_up(current_position)
            elif direction == Directions.RIGHT:
                new_position = self.move_right(current_position)
            elif direction == Directions.DOWN:
                new_position = self.move_down(current_position)
            elif direction == Directions.LEFT:
                new_position = self.move_left(current_position)

            # Check if the individual tried to move outside the maze or into a wall
            if new_position == current_position or self.maze[new_position[0]][new_position[1]] == 0:
                return distance_from_exit(current_position, self.end)

            # Check if the individual reached the exit
            current_position = new_position
            if self.maze[current_position[0]][current_position[1]] == 3:
                return 0 - (individual.size() - i)

        # If the individual didn't reach the exit, return the distance to the exit
        return distance_from_exit(current_position, self.end)

    def move_left(self, position):
        if position[1] > 0:
            return position[0], position[1] - 1
        return position

    def move_right(self, position):
        if position[1] < self.m - 1:
            return position[0], position[1] + 1
        return position

    def move_up(self, position):
        if position[0] > 0:
            return position[0] - 1, position[1]
        return position

    def move_down(self, position):
        if position[0] < self.n - 1:
            return position[0] + 1, position[1]
        return position


def distance_from_exit(current_position, end_position):
    return abs(current_position[0] - end_position[0]) + abs(current_position[1] - end_position[1])
