# Activity 5: Stacks and Queues — Array vs. Linked List

## Program description

This project demonstrates the **LIFO (Last In, First Out)** rule of stacks and the **FIFO (First In, First Out)** rule of queues. It implements both structures using arrays and linked lists. The program includes a menu for testing operations, error handling, a balanced-parentheses checker, and a print queue simulation.

## Files

| File | Description |
|---|---|
| `node.py` | Node class shared by the linked implementations. |
| `array_stack.py` | Fixed-capacity array stack. |
| `linked_stack.py` | Stack using linked nodes. |
| `array_queue.py` | Circular fixed-capacity array queue. |
| `linked_queue.py` | Queue using head and tail references. |
| `applications.py` | Balanced-parentheses checker and print queue exercise. |
| `main.py` | Main menu and test driver. |
| `analysis.md` | Answer to the laboratory analysis question. |
| `sample_runs.md` | Example program runs and error handling. |

## Requirements

- Python 3.8 or newer
- No extra Python packages are required.

## How to run

1. Download or clone this repository.
2. Open the project folder in Visual Studio Code, PyCharm, or a terminal.
3. Open a terminal in the project folder.
4. Run:

   ```bash
   python main.py
   ```

5. Select an implementation from the main menu.
6. For array implementations, enter a capacity when asked.
7. Select an operation and follow the prompts. The program displays the structure after each operation.

## Operations

### Stack
- `push(value)`: add an item to the top.
- `pop()`: remove and return the top item.
- `peek()`: view the top item without removing it.
- `is_empty()`: check whether the stack is empty.
- `is_full()`: check whether the fixed array stack is full. A linked stack has no fixed capacity and returns `False`.

### Queue
- `enqueue(value)`: add an item at the rear.
- `dequeue()`: remove and return the front item.
- `peek_front()`: view the front item without removing it.
- `is_empty()`: check whether the queue is empty.
- `is_full()`: check whether the fixed array queue is full. A linked queue has no fixed capacity and returns `False`.

## Error handling

The array stack and array queue raise `OverflowError` when an item is added while full. Stack and queue removal or peek operations raise `IndexError` when the structure is empty. The menu catches these exceptions and displays a descriptive error message.

## Circular queue wrap-around

For a circular array queue, the next rear position is calculated with:

```python
rear = (front + size) % len(data)
```

The front position also moves using modulo after a dequeue. This lets the queue reuse empty positions at the beginning of the array.

## Application exercises

Choose **5. Run Application Exercises** from the main menu. Enter a bracket expression to check whether its parentheses, square brackets, and curly braces are balanced. The program then adds sample print jobs and processes them in FIFO order.

## Notes

All source files should stay in the same project folder so that the imports work correctly.
