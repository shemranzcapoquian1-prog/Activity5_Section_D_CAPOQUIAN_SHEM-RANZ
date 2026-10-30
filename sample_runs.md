# Sample Runs

These are example runs. Your exact prompts and spacing may look slightly different depending on the terminal.

## 1. Array stack overflow

```text
Choose an implementation: 1
Enter stack capacity: 2
Choose an operation: 1
Enter a value: A
Value added successfully.
Current state: Stack (bottom -> top): ['A']
Choose an operation: 1
Enter a value: B
Value added successfully.
Current state: Stack (bottom -> top): ['A', 'B']
Choose an operation: 1
Enter a value: C
ERROR: Stack overflow: cannot push because the stack is full.
Structure was not changed.
Current state: Stack (bottom -> top): ['A', 'B']
```

## 2. Array stack underflow

```text
Choose an implementation: 1
Enter stack capacity: 2
Choose an operation: 2
ERROR: Stack underflow: cannot pop because the stack is empty.
Structure was not changed.
Current state: Stack (bottom -> top): []
```

## 3. Circular array queue wrap-around

```text
Choose an implementation: 3
Enter queue capacity: 3
Enqueue A
Enqueue B
Enqueue C
Dequeue -> A
Dequeue -> B
Enqueue D
Enqueue E
Current queue (front -> rear): ['C', 'D', 'E']
```

After removing A and B, the front moves forward. D and E are stored in the freed positions by wrapping around to the start of the array.

## 4. Array queue overflow and underflow

```text
Queue capacity: 2
Enqueue A
Enqueue B
Enqueue C
ERROR: Queue overflow: cannot enqueue because the queue is full.

Dequeue -> A
Dequeue -> B
Dequeue
ERROR: Queue underflow: cannot dequeue because the queue is empty.
```

## 5. Linked queue returns to empty

```text
Enqueue A
Dequeue -> A
Queue (front -> rear): []
```

When the last item is removed, both the front and rear references become None.
