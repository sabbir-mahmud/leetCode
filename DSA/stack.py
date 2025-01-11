from collections import deque
from typing import Generic, TypeVar

# Define a generic type variable 'T' to allow the stack to hold any type
T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self):
        """Initialize the stack with an empty deque container."""
        # A deque is a double-ended queue, providing fast append and pop operations from both ends.
        # It's ideal for implementing a stack since both push and pop operations are O(1) in a deque.
        self._container = deque()

    def push(self, val: T) -> None:
        """
        Push a value onto the stack.

        Args:
            val: The value to be added to the stack.

        This method appends the value to the end of the deque, which corresponds to the "top" of the stack.
        """
        self._container.append(val)

    def pop(self) -> T:
        """
        Remove and return the top value from the stack.

        Returns:
            The value at the top of the stack.

        Raises:
            IndexError: If the stack is empty.

        This method removes and returns the item from the top of the stack (the right end of the deque).
        If the stack is empty, it raises an IndexError, which is standard for stack operations.
        """
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self._container.pop()

    def peek(self) -> T:
        """
        Return the top value of the stack without removing it.

        Returns:
            The value at the top of the stack.

        Raises:
            IndexError: If the stack is empty.

        This method returns the value at the top of the stack (the last element in the deque),
        but it doesn't remove it. This is useful for inspecting the top value without modifying the stack.
        """
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self._container[-1]

    def is_empty(self) -> bool:
        """
        Check if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.

        This method checks whether the deque is empty (equivalent to checking len(self._container) == 0).
        It returns a boolean indicating if there are any items in the stack.
        """
        return not self._container

    def size(self) -> int:
        """
        Get the number of items in the stack.

        Returns:
            The number of items in the stack.

        This method returns the size of the stack by returning the length of the deque.
        It's an O(1) operation since deque has a size property.
        """
        return len(self._container)


# Example usage of the Stack class
if __name__ == "__main__":
    stack = Stack[int]()  # Create a stack for integers

    # Push values onto the stack
    stack.push(10)
    stack.push(20)
    stack.push(30)

    # Peek the top value
    print("Top value:", stack.peek())  # Output: 30

    # Get the size of the stack
    print("Size of stack:", stack.size())  # Output: 3

    # Pop the top value from the stack
    print("Popped value:", stack.pop())  # Output: 30

    # Check if the stack is empty
    print("Is stack empty?", stack.is_empty())  # Output: False

    # Pop all remaining values
    stack.pop()
    stack.pop()

    # Check if the stack is empty now
    print("Is stack empty now?", stack.is_empty())  # Output: True

    # Reverse a string using a stack
    def reverse_string(text: str) -> str:
        """
        Reverse the input string using a stack.

        Args:
            text: The string to be reversed.

        Returns:
            The reversed string.

        The method pushes each character of the string onto the stack and pops them out in reverse order
        to build the reversed string.
        """
        stack = Stack[str]()  # Create a stack for characters
        for char in text:
            stack.push(char)

        reverse_text = ""
        # Pop characters from the stack to form the reversed string
        while stack.size() != 0:
            reverse_text += f"{stack.pop()}"

        return reverse_text

    print(
        reverse_string("We will conquere COVID-19")
    )  # Output: "91-DIVOC ereuqnoc lliw eW"

    # Check if the parentheses in a string are balanced using a stack
    def is_balanced(text: str) -> bool:
        """
        Check if the parentheses (or other brackets) in the input string are balanced.

        Args:
            text: The string to check for balanced parentheses.

        Returns:
            True if the parentheses are balanced, False otherwise.

        This method uses a stack to ensure that each opening bracket has a corresponding closing bracket
        in the correct order.
        """
        stack = Stack[str]()  # Create a stack to hold the opening parentheses
        matching_pairs = {")": "(", "}": "{", "]": "["}  # Dictionary for matching pairs
        is_balanced = True  # Assume the string is balanced initially

        for char in text:
            # If the character is an opening parenthesis, push it onto the stack
            if char in "({[":
                stack.push(char)
            # If the character is a closing parenthesis, check if it matches the top of the stack
            elif char in ")}]":
                # If the stack is empty or the top doesn't match, it's unbalanced
                if stack.is_empty() or stack.pop() != matching_pairs[char]:
                    is_balanced = False
                    break

        # If the stack is not empty after processing all characters, it's unbalanced
        if not stack.is_empty():
            is_balanced = False

        return is_balanced

    # Example checks for balanced parentheses
    print(is_balanced("({a+b})"))  # Output: True
    print(is_balanced("))((a+b}{"))  # Output: False
    print(is_balanced("((a+b))"))  # Output: True
    print(is_balanced("))"))  # Output: False
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))  # Output: True
