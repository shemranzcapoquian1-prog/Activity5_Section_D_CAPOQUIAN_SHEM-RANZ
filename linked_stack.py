"""Stack implemented with a singly linked list."""


from node import Node


class LinkedStack:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.top is None

    def is_full(self):
        # A linked stack has no fixed capacity.
        return False

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: cannot pop because the stack is empty.")
        value = self.top.value
        self.top = self.top.next
        self.size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty: there is no top element to view.")
        return self.top.value

    def to_list(self):
        """Return values from bottom to top for easy display."""
        values = []
        current = self.top
        while current is not None:
            values.append(current.value)
            current = current.next
        values.reverse()
        return values

    def __str__(self):
        return f"Stack (bottom -> top): {self.to_list()}"
