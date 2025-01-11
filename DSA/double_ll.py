class Node:
    """
    Represents a single node in the doubly linked list.
    Attributes:
        data: The data stored in the node.
        next: A reference to the next node in the linked list.
        prev: A reference to the previous node in the linked list.
    """

    def __init__(self, data, next=None, prev=None):
        """
        Initialize a new Node with data, and optionally with references to the next and previous nodes.
        Parameters:
            data: The data to store in the node.
            next: Reference to the next node (default is None).
            prev: Reference to the previous node (default is None).
        """
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    """
    Implements a doubly linked list with various utility methods for insertion, deletion, traversal, and more.
    Attributes:
        head: Points to the first node in the linked list.
        tail: Points to the last node in the linked list, allowing efficient operations at the end of the list.
    """

    def __init__(self):
        """
        Initialize an empty doubly linked list with head and tail set to None.
        """
        self.head = None
        self.tail = None

    def insert_at_beg(self, data):
        """
        Insert a new node at the beginning of the linked list.
        Parameters:
            data: The data to be stored in the new node.
        """
        # Create a new node with the current head as its next reference
        node = Node(data, next=self.head)
        if self.head:
            # Update the previous reference of the existing head node
            self.head.prev = node
        else:
            # If the list is empty, the new node is both head and tail
            self.tail = node
        # Update the head to the new node
        self.head = node

    def insert_at_end(self, data):
        """
        Insert a new node at the end of the linked list.
        Parameters:
            data: The data to be stored in the new node.
        """
        # Create a new node with the current tail as its previous reference
        node = Node(data, prev=self.tail)
        if self.tail:
            # Update the next reference of the existing tail node
            self.tail.next = node
        else:
            # If the list is empty, the new node is both head and tail
            self.head = node
        # Update the tail to the new node
        self.tail = node

    def insert_values(self, data_list):
        """
        Insert multiple values into the linked list. Clears the existing list before insertion.
        Parameters:
            data_list: A list of values to insert.
        """
        # Clear the linked list
        self.head = None
        self.tail = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self, target_value, new_value):
        """
        Insert a new node with the given new_value after the first occurrence of target_value.
        Parameters:
            target_value: The value after which the new node is to be inserted.
            new_value: The data for the new node.
        """
        itr = self.head
        while itr:
            if itr.data == target_value:
                # Create a new node between itr and itr.next
                node = Node(new_value, next=itr.next, prev=itr)
                if itr.next:  # Update the next node's previous reference if it exists
                    itr.next.prev = node
                else:  # If adding after the tail, update the tail reference
                    self.tail = node
                itr.next = node
                return
            itr = itr.next
        print(f"Value {target_value} not found in the list.")

    def remove_at_index(self, index):
        """
        Remove the node at the specified index.
        Parameters:
            index: The zero-based index of the node to remove.
        """
        if index < 0 or index >= self.length():
            print("Invalid index!")
            return

        if index == 0:  # Special case: removing the head
            if self.head.next:
                self.head = self.head.next
                self.head.prev = None
            else:  # If there's only one node
                self.head = None
                self.tail = None
            return

        itr = self.head
        count = 0
        while itr:
            if count == index:
                if itr.next:  # Update the next node's previous reference
                    itr.next.prev = itr.prev
                else:  # If removing the tail, update the tail reference
                    self.tail = itr.prev
                if itr.prev:  # Update the previous node's next reference
                    itr.prev.next = itr.next
                return
            itr = itr.next
            count += 1

    def remove_by_value(self, value):
        """
        Remove the first node with the specified value.
        Parameters:
            value: The value of the node to be removed.
        """
        itr = self.head
        while itr:
            if itr.data == value:
                if itr.next:  # Update the next node's previous reference
                    itr.next.prev = itr.prev
                else:  # If removing the tail, update the tail reference
                    self.tail = itr.prev
                if itr.prev:  # Update the previous node's next reference
                    itr.prev.next = itr.next
                else:  # If removing the head, update the head reference
                    self.head = itr.next
                return
            itr = itr.next
        print(f"Value {value} not found in the list.")

    def reverse(self):
        """
        Reverse the doubly linked list in place by swapping the next and previous pointers of all nodes.
        """
        curr = self.head
        self.tail = self.head  # Update the tail to the current head
        prev = None
        while curr:
            prev = curr.prev
            curr.prev = curr.next
            curr.next = prev
            curr = curr.prev
        if prev:
            # Update the head to the new first node
            self.head = prev.prev

    def print_forward(self):
        """
        Print the elements of the linked list in forward order.
        """
        if self.head is None:
            print("Linked list is empty.")
            return

        itr = self.head
        ll_str = ""
        while itr:
            ll_str += f"{itr.data} <--> "
            itr = itr.next
        print(ll_str + "None")

    def print_backward(self):
        """
        Print the elements of the linked list in reverse order, starting from the tail.
        """
        if self.tail is None:
            print("Linked list is empty.")
            return

        itr = self.tail
        ll_str = ""
        while itr:
            ll_str += f"{itr.data} <--> "
            itr = itr.prev
        print(ll_str + "None")

    def length(self):
        """
        Calculate and return the length of the linked list.
        Returns:
            int: The number of nodes in the linked list.
        """
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def find(self, value):
        """
        Search for a value in the linked list.
        Parameters:
            value: The value to search for.
        Returns:
            bool: True if the value is found, False otherwise.
        """
        itr = self.head
        while itr:
            if itr.data == value:
                return True
            itr = itr.next
        return False


# Testing the DoublyLinkedList class
if __name__ == "__main__":
    dll = DoublyLinkedList()

    # Insert multiple values
    dll.insert_values([1, 2, 3, 4, 5])
    dll.print_forward()

    # Insert at beginning and end
    dll.insert_at_beg(0)
    dll.insert_at_end(6)
    dll.print_forward()

    # Print backward
    dll.print_backward()

    # Remove by index and value
    dll.remove_at_index(3)
    dll.remove_by_value(5)
    dll.print_forward()

    # Insert after a specific value
    dll.insert_after_value(4, 7)
    dll.print_forward()

    # Reverse the doubly linked list
    dll.reverse()
    dll.print_forward()

    # Find a value
    print("Find 7:", dll.find(7))
    print("Find 99:", dll.find(99))

    # Print length
    print("Length of doubly linked list:", dll.length())
