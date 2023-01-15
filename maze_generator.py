import random
from random import randint

import matplotlib.pyplot as plt

from stack import Stack


def break_walls(maze):
    rows = len(maze)
    cols = len(maze[0])
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 0 and random.random() < 0.1:
                maze[i][j] = 1


def visualize_maze(maze, run_start_time):
    print("Generated maze:")
    print("----------------------------")
    for line in maze:
        print(line)
    print("----------------------------\n")

    maze_file_name = f'./output/{run_start_time}_maze.png'
    print(f'Visual representation of the maze saved to {maze_file_name}')
    fig = plt.figure(figsize=(10, 10))
    plt.imshow(maze, cmap='flag')
    plt.savefig(maze_file_name)
    plt.close(fig)


def generator(rows, cols, maze_start, maze_exit):
    # Init maze and helper arrays
    maze = list(list(0 for _ in range(cols))
                for _ in range(rows))
    visited = list(list(False for _ in range(cols))
                   for _ in range(rows))
    parent = list(list((-1, -1)
                       for _ in range(cols)) for _ in range(rows))

    # Init stack with start position
    maze_builder_stack = Stack()
    maze_builder_stack.push(maze_start)

    while not maze_builder_stack.is_empty():
        x, y = maze_builder_stack.pop()
        visited[x][y] = True

        # Mark the current cell as walkable only if it won't cause a loop
        if (x + 1 < rows) and maze[x + 1][y] == 1 \
                and parent[x][y] != (x + 1, y):
            continue
        if (0 < x) and maze[x - 1][y] == 1 \
                and parent[x][y] != (x - 1, y):
            continue
        if (y + 1 < cols) and maze[x][y + 1] == 1 \
                and parent[x][y] != (x, y + 1):
            continue
        if (y > 0) and maze[x][y - 1] == 1 \
                and parent[x][y] != (x, y - 1):
            continue
        maze[x][y] = 1

        # Add the current cell's unvisited neighbors to the stack in a random order
        neighbours = []
        if (x + 1 < rows) and visited[x + 1][y] is False:
            visited[x + 1][y] = True
            neighbours.append((x + 1, y))
            parent[x + 1][y] = (x, y)

        if (0 < x) and visited[x - 1][y] is False:
            visited[x - 1][y] = True
            neighbours.append((x - 1, y))
            parent[x - 1][y] = (x, y)

        if (y + 1 < cols) and visited[x][y + 1] is False:
            visited[x][y + 1] = True
            neighbours.append((x, y + 1))
            parent[x][y + 1] = (x, y)

        if (y > 0) and visited[x][y - 1] is False:
            visited[x][y - 1] = True
            neighbours.append((x, y - 1))
            parent[x][y - 1] = (x, y)

        # Shuffle the neighbors and add them to the stack
        # Check if the neighbor is the exit to make sure it is the last one to be added, so it is the first to be popped
        exit_cell_found = False
        while len(neighbours):
            neighbour = neighbours.pop(randint(0, len(neighbours) - 1))
            if neighbour == maze_exit:
                exit_cell_found = True
                continue
            maze_builder_stack.push(neighbour)

        if exit_cell_found:
            maze_builder_stack.push(maze_exit)

    # Finally, mark the entrance and exit cells as with their distinct values
    maze[maze_start[0]][maze_start[1]] = 2
    maze[maze_exit[0]][maze_exit[1]] = 3

    break_walls(maze)
    return maze


def random_maze_generator(rows, cols, maze_start, maze_exit, run_start_time):
    maze = generator(rows, cols, maze_start, maze_exit)
    visualize_maze(maze, run_start_time)

    return maze
