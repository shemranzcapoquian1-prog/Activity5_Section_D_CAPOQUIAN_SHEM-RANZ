"""Fixed-capacity stack implemented with a Python list."""


class ArrayStack:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Stack capacity must be greater than zero.")
        self.data = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == len(self.data) - 1

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack overflow: cannot push because the stack is full.")
        self.top += 1
        self.data[self.top] = value

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: cannot pop because the stack is empty.")
        value = self.data[self.top]
        self.data[self.top] = None
        self.top -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty: there is no top element to view.")
        return self.data[self.top]

    def to_list(self):
        """Return the current stack from bottom to top."""
        return self.data[:self.top + 1]

    def __str__(self):
        return f"Stack (bottom -> top): {self.to_list()}"
