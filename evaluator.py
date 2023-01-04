import random


def generate_maze(maze, x, y):
    # base case: if the current cell is outside the maze or has already been visited, return
    if x < 0 or y < 0 or x >= len(maze) or y >= len(maze[0]) or maze[x][y] == 1:
        return

    # mark the current cell as visited
    maze[x][y] = 1

    # shuffle the list of directions
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    random.shuffle(directions)

    # try moving to a random unvisited neighbor
    for dx, dy in directions:
        generate_maze(maze, x + dx, y + dy)


# create an empty maze
maze = [[0 for y in range(10)] for x in range(10)]

# mark the entry and exit points
maze[0][0] = 1
maze[9][9] = 1

# start the recursive backtracking from the entry point
generate_maze(maze, 0, 0)

# print the resulting maze
for row in maze:
    print(row)
