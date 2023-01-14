from random import randint


# Class to define structure of a node
class Node:
    def __init__(self, value=None,
                 next_element=None):
        self.val = value
        self.next = next_element


# Class to implement a stack
class Stack:

    # Constructor
    def __init__(self):
        self.head = None
        self.length = 0

    # Put an item on the top of the stack
    def insert(self, data):
        self.head = Node(data, self.head)
        self.length += 1

    # Return the top position of the stack
    def pop(self):
        if self.length == 0:
            return None
        else:
            returned = self.head.val
            self.head = self.head.next
            self.length -= 1
            return returned

    # Return False if the stack is empty
    # and true otherwise
    def not_empty(self):
        return bool(self.length)

    # Return the top position of the stack
    def top(self):
        return self.head.val


# Function to generate the random maze
def random_maze_generator(n, m, start, end):
    rows, cols = n, m

    # Array with only walls (where paths will
    # be created)
    maze = list(list(0 for _ in range(cols))
                for _ in range(rows))

    # Auxiliary matrices to avoid cycles
    visited = list(list(False for _ in range(cols))
                   for _ in range(rows))
    previous = list(list((-1, -1)
                         for _ in range(cols)) for _ in range(rows))

    s = Stack()

    # Insert initial position
    s.insert(start)

    # Keep walking on the graph using dfs
    # until we have no more paths to traverse
    # (create)
    while s.not_empty():

        # Remove the position of the Stack
        # and mark it as visited
        x, y = s.pop()
        visited[x][y] = True

        # Check if it will create a cycle
        # if the adjacent position is valid
        # (is in the maze) and the position
        # is not already marked as a path
        # (was traversed during the dfs) and
        # this position is not the one before it
        # in the dfs path it means that
        # the current position must not be marked.

        # This is to avoid cycles with adj positions
        if (x + 1 < rows) and maze[x + 1][y] == 1 \
                and previous[x][y] != (x + 1, y):
            continue
        if (0 < x) and maze[x - 1][y] == 1 \
                and previous[x][y] != (x - 1, y):
            continue
        if (y + 1 < cols) and maze[x][y + 1] == 1 \
                and previous[x][y] != (x, y + 1):
            continue
        if (y > 0) and maze[x][y - 1] == 1 \
                and previous[x][y] != (x, y - 1):
            continue

        # Mark as walkable position
        maze[x][y] = 1

        # Array to shuffle neighbours before
        # insertion
        to_stack = []

        # Before inserting any position,
        # check if it is in the boundaries of
        # the maze
        # and if it were visited (to avoid cycles)

        # If adj position is valid and was not visited yet
        if (x + 1 < rows) and visited[x + 1][y] is False:
            # Mark the adj position as visited
            visited[x + 1][y] = True

            # Memorize the position to insert the
            # position in the stack
            to_stack.append((x + 1, y))

            # Memorize the current position as its
            # previous position on the path
            previous[x + 1][y] = (x, y)

        if (0 < x) and visited[x - 1][y] is False:
            # Mark the adj position as visited
            visited[x - 1][y] = True

            # Memorize the position to insert the
            # position in the stack
            to_stack.append((x - 1, y))

            # Memorize the current position as its
            # previous position on the path
            previous[x - 1][y] = (x, y)

        if (y + 1 < cols) and visited[x][y + 1] is False:
            # Mark the adj position as visited
            visited[x][y + 1] = True

            # Memorize the position to insert the
            # position in the stack
            to_stack.append((x, y + 1))

            # Memorize the current position as its
            # previous position on the path
            previous[x][y + 1] = (x, y)

        if (y > 0) and visited[x][y - 1] is False:
            # Mark the adj position as visited
            visited[x][y - 1] = True

            # Memorize the position to insert the
            # position in the stack
            to_stack.append((x, y - 1))

            # Memorize the current position as its
            # previous position on the path
            previous[x][y - 1] = (x, y)

        # Indicates if Pf is a neighbour position
        pf_flag = False
        while len(to_stack):

            # Remove random position
            neighbour = to_stack.pop(randint(0, len(to_stack) - 1))

            # Is the final position,
            # remember that by marking the flag
            if neighbour == end:
                pf_flag = True

            # Put on the top of the stack
            else:
                s.insert(neighbour)

        # This way, Pf will be on the top
        if pf_flag:
            s.insert(end)

    # Mark the initial position
    x0, y0 = start
    xf, yf = end
    maze[x0][y0] = 2
    maze[xf][yf] = 3

    # Return maze formed by the traversed path
    for line in maze:
        print(line)
    return maze
