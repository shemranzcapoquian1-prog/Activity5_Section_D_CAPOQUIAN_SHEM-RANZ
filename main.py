"""Menu-driven test program for all four stack and queue implementations."""


from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue
from applications import run_applications


def show_state(structure):
    print("Current state:", structure)
    print("Empty:", structure.is_empty())
    print("Full:", structure.is_full())


def run_structure(structure, kind):
    """Display and run the operations available for the selected structure."""
    while True:
        print("\nSelected structure:", kind)
        if kind.endswith("Stack"):
            print("1. Push")
            print("2. Pop")
            print("3. Peek")
        else:
            print("1. Enqueue")
            print("2. Dequeue")
            print("3. Peek front")
        print("4. Check if empty")
        print("5. Check if full")
        print("0. Back to main menu")

        choice = input("Choose an operation: ").strip()
        try:
            if choice == "1":
                value = input("Enter a value: ")
                if kind.endswith("Stack"):
                    structure.push(value)
                else:
                    structure.enqueue(value)
                print("Value added successfully.")
                show_state(structure)

            elif choice == "2":
                value = structure.pop() if kind.endswith("Stack") else structure.dequeue()
                print("Removed value:", value)
                show_state(structure)

            elif choice == "3":
                value = structure.peek() if kind.endswith("Stack") else structure.peek_front()
                print("Top/front value:", value)
                show_state(structure)

            elif choice == "4":
                print("Is empty?", structure.is_empty())
                show_state(structure)

            elif choice == "5":
                print("Is full?", structure.is_full())
                show_state(structure)

            elif choice == "0":
                break
            else:
                print("Invalid choice. Please select from the menu.")

        except (IndexError, OverflowError, ValueError) as error:
            print("ERROR:", error)
            print("Structure was not changed.")
            show_state(structure)


def choose_capacity(label):
    while True:
        try:
            capacity = int(input(f"Enter {label} capacity: "))
            if capacity <= 0:
                print("Capacity must be greater than zero.")
                continue
            return capacity
        except ValueError:
            print("Please enter a whole number.")


def main():
    while True:
        print("\n========== STACKS AND QUEUES ==========")
        print("1. Array Stack")
        print("2. Linked Stack")
        print("3. Circular Array Queue")
        print("4. Linked Queue")
        print("5. Run Application Exercises")
        print("0. Exit")

        choice = input("Choose an implementation: ").strip()

        if choice == "1":
            capacity = choose_capacity("stack")
            run_structure(ArrayStack(capacity), "ArrayStack")
        elif choice == "2":
            run_structure(LinkedStack(), "LinkedStack")
        elif choice == "3":
            capacity = choose_capacity("queue")
            run_structure(ArrayQueue(capacity), "ArrayQueue")
        elif choice == "4":
            run_structure(LinkedQueue(), "LinkedQueue")
        elif choice == "5":
            run_applications()
        elif choice == "0":
            print("Thank you for using the program!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
