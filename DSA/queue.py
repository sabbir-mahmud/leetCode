import threading
import time
from collections import deque


class Queue:
    """
    A simple queue implementation using deque from the collections module.
    It supports standard queue operations like enqueue, dequeue,
    checking if the queue is empty, and getting the queue size.
    """

    def __init__(self):
        # Initialize the queue with an empty deque.
        # deque is a high-performance list for adding/removing elements from both ends.
        self.buffer = deque()

    def enqueue(self, val):
        """
        Adds an element to the end of the queue.
        This is an O(1) operation as appending to the right end of a deque is fast.
        """
        self.buffer.append(val)

    def dequeue(self):
        """
        Removes and returns an element from the front of the queue.
        This is an O(1) operation as popping from the left end of a deque is fast.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")  # Avoid errors on empty queue.
        return self.buffer.popleft()

    def is_empty(self):
        """
        Checks if the queue is empty.
        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self.buffer) == 0

    def size(self):
        """
        Returns the number of elements in the queue.
        This is an O(1) operation, as deque maintains the size.
        """
        return len(self.buffer)

    def front(self):
        """
        Returns the element at the front of the queue without removing it.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Front from empty queue")
        return self.buffer[0]


def binary_writer(number):
    """
    Generates binary numbers from 1 to 'number' using a queue-based approach.
    This approach generates binary numbers in the order by enqueuing and dequeuing.

    Args:
        number (int): The number of binary numbers to generate.
    """
    queue = Queue()

    # Start with the binary number '1'
    queue.enqueue("1")

    # Generate binary numbers and print them
    for _ in range(number):
        # Get the front binary number
        front = queue.front()

        # Print the current binary number
        print(front)

        # Enqueue the next numbers formed by appending '0' and '1'
        queue.enqueue(front + "0")
        queue.enqueue(front + "1")

        # Dequeue the front number to process the next
        queue.dequeue()


def main():
    """
    Demonstrates the use of the Queue class with enqueue, dequeue, size,
    and empty checks, along with binary number generation and threaded food order simulation.
    """
    # Create a new queue instance
    queue = Queue()

    # Enqueue elements
    print("Enqueuing elements:")
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)

    # Display the queue size
    print(f"Queue size after enqueuing: {queue.size()}")

    # Dequeue and display the removed element
    print("\nDequeuing elements:")
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Dequeued: {queue.dequeue()}")

    # Check the queue size after dequeuing
    print(f"\nQueue size after dequeuing: {queue.size()}")

    # Check if the queue is empty
    print(f"\nIs the queue empty? {queue.is_empty()}")

    # Dequeue remaining elements
    print("\nDequeuing remaining elements:")
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Dequeued: {queue.dequeue()}")

    # Check the final queue size
    print(f"\nQueue size after all dequeuing: {queue.size()}")

    # Check if the queue is empty after all operations
    print(f"\nIs the queue empty? {queue.is_empty()}")

    # Generate binary numbers from 1 to 10
    print("\nBinary Writer Output:")
    binary_writer(10)

    # Create a food order queue and simulate order placing and serving using threads
    food_order = Queue()

    def place_orders(orders):
        """
        Simulates placing orders by enqueuing them to the queue.
        Introduces a 0.5-second delay between each order for realism.

        Args:
            orders (list): List of food orders to be placed.
        """
        for order in orders:
            print("Placing order --> ", order)
            food_order.enqueue(order)
            time.sleep(0.5)  # Simulate a short delay in placing orders.

    def serve_orders():
        """
        Simulates serving orders by dequeuing them from the queue and printing the served order.
        Introduces a 2-second delay between serving each order for realism.
        """
        while True:
            order = food_order.dequeue()
            print("Serving order --> ", order)
            time.sleep(2)  # Simulate a delay in serving each order.

    # List of food orders
    orders = ["pizza", "samosa", "pasta", "biryani", "burger"]

    # Create threads to place and serve orders
    t1 = threading.Thread(target=place_orders, args=(orders,))
    t2 = threading.Thread(target=serve_orders)

    # Start the threads
    t1.start()
    t2.start()


# Entry point for the program
if __name__ == "__main__":
    main()
