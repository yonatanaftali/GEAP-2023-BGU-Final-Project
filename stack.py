class Node:
    def __init__(self, value=None,
                 next_element=None):
        self.val = value
        self.next = next_element


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, data):
        self.head = Node(data, self.head)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        else:
            popped = self.head.val
            self.head = self.head.next
            self.size -= 1
            return popped

    def peek(self):
        return self.head.val

    def is_empty(self):
        return not bool(self.size)
