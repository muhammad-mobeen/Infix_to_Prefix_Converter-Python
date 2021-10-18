from collections import deque


class Stack():
    def __init__(self) -> None:
        self.control = deque

    def push(self, val):
        self.control.append(val)

    def pop(self):
        return self.control.pop()

    def size(self):
        return len(self.control)
    
    def is_empty(self):
        return len(self.control) == 0