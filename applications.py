"""Practical applications of stacks and queues."""


from array_stack import ArrayStack
from linked_queue import LinkedQueue


def is_balanced(expression):
    """Check whether (), [] and {} are correctly paired and nested."""
    stack = ArrayStack(max(1, len(expression)))
    matching_open = {")": "(", "]": "[", "}": "{"}
    opening = set(matching_open.values())

    for character in expression:
        if character in opening:
            stack.push(character)
        elif character in matching_open:
            if stack.is_empty() or stack.pop() != matching_open[character]:
                return False

    return stack.is_empty()


def print_queue_demo():
    """Add print jobs and process them in first-in, first-out order."""
    jobs = [
        {"id": "JOB-101", "pages": 5},
        {"id": "JOB-102", "pages": 2},
        {"id": "JOB-103", "pages": 8},
    ]

    queue = LinkedQueue()
    print("\nAdding print jobs:")
    for job in jobs:
        queue.enqueue(job)
        print(f"Added {job['id']} ({job['pages']} pages). Queue: {queue}")

    print("\nPrinting jobs in FIFO order:")
    wait_position = 1
    while not queue.is_empty():
        job = queue.dequeue()
        print(
            f"Wait position {wait_position}: printing {job['id']} "
            f"({job['pages']} pages)."
        )
        wait_position += 1


def run_applications():
    print("\n--- Application 1: Balanced Parentheses ---")
    expression = input("Enter an expression containing brackets: ")
    if is_balanced(expression):
        print("Result: The brackets are balanced.")
    else:
        print("Result: The brackets are NOT balanced.")

    print("\n--- Application 2: Print Queue Simulation ---")
    print_queue_demo()
