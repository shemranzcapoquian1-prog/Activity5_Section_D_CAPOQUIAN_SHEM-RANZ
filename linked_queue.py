"""Queue implemented with a singly linked list and head/tail references."""


from node import Node


class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.front is None

    def is_full(self):
        # A linked queue has no fixed capacity.
        return False

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.front = node
        else:
            self.rear.next = node
        self.rear = node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: cannot dequeue because the queue is empty.")
        value = self.front.value
        self.front = self.front.next
        self.size -= 1
        if self.front is None:
            self.rear = None
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty: there is no front element to view.")
        return self.front.value

    def to_list(self):
        values = []
        current = self.front
        while current is not None:
            values.append(current.value)
            current = current.next
        return values

    def __str__(self):
        return f"Queue (front -> rear): {self.to_list()}"
