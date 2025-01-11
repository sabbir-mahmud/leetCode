class Node:
    """
    Represents a single node in the linked list.
    Attributes:
        data: The data value stored in the node.
        next: A reference to the next node in the linked list.
    """

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    """
    Implements a singly linked list with various utility methods for insertion, deletion, and traversal.
    Attributes:
        head: Points to the first node in the linked list.
    """

    def __init__(self):
        self.head = None  # Initialize an empty linked list

    def insert_at_beg(self, data):
        """
        Insert a new node at the beginning of the linked list.
        """
        node = Node(
            data, self.head
        )  # Create a new node with current head as its next reference
        self.head = node  # Update head to the new node

    def insert_at_end(self, data):
        """
        Insert a new node at the end of the linked list.
        """
        if self.head is None:  # If the linked list is empty
            self.head = Node(data)  # Set the new node as the head
            return

        itr = self.head
        while itr.next:  # Traverse to the last node
            itr = itr.next
        itr.next = Node(data)  # Append the new node at the end

    def insert_values(self, data_list, at_end=True):
        """
        Insert multiple values into the linked list.
        Parameters:
            data_list: A list of values to insert.
            at_end: Insert at the end if True, otherwise at the beginning.
        """
        self.head = None  # Clear the list
        if at_end:
            for data in data_list:
                self.insert_at_end(data)
        else:
            for data in data_list:
                self.insert_at_beg(data)

    def insert_after_value(self, target_value, new_value):
        """
        Insert a new node after the first occurrence of the target value.
        """
        itr = self.head
        while itr:
            if itr.data == target_value:
                itr.next = Node(new_value, itr.next)
                return
            itr = itr.next
        print(f"Value {target_value} not found in the list.")

    def remove_at_index(self, index):
        """
        Remove the node at the specified index.
        """
        if index < 0 or index >= self.length():
            print("Invalid index!")
            return

        if index == 0:  # Special case: removing the head
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next  # Bypass the target node
                return
            itr = itr.next
            count += 1

    def insert_at_index(self, index, data):
        """
        Insert a new node at the specified index.
        """
        if index < 0 or index > self.length():
            print("Invalid index!")
            return

        if index == 0:  # Special case: inserting at the beginning
            self.insert_at_beg(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)  # Insert the new node
                return
            itr = itr.next
            count += 1

    def remove_by_value(self, value):
        """
        Remove the first node with the specified value.
        """
        if self.head is None:  # If the list is empty
            print("Linked list is empty.")
            return

        if self.head.data == value:  # Special case: removing the head
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == value:
                itr.next = itr.next.next  # Bypass the node with the value
                return
            itr = itr.next
        print(f"Value {value} not found in the list.")

    def reverse(self):
        """
        Reverse the linked list.
        """
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next  # Save the next node
            curr.next = prev  # Reverse the link
            prev = curr  # Move prev to current
            curr = next_node  # Move current to next
        self.head = prev  # Update head to the new front of the list

    def print(self):
        """
        Print the elements of the linked list in a readable format.
        """
        if self.head is None:
            print("Linked list is empty.")
            return

        itr = self.head
        ll_str = ""
        while itr:
            ll_str += f"{itr.data} --> "
            itr = itr.next
        print(ll_str + "None")

    def length(self):
        """
        Calculate and return the length of the linked list.
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
        Returns True if found, otherwise False.
        """
        itr = self.head
        while itr:
            if itr.data == value:
                return True
            itr = itr.next
        return False


# Testing the LinkedList class
if __name__ == "__main__":
    ll = LinkedList()

    # Insert multiple values
    ll.insert_values([1, 2, 3, 4, 5])
    ll.print()

    # Insert at beginning and end
    ll.insert_at_beg(0)
    ll.insert_at_end(6)
    ll.print()

    # Remove by index and value
    ll.remove_at_index(3)
    ll.remove_by_value(5)
    ll.print()

    # Insert at specific index
    ll.insert_at_index(2, 10)
    ll.print()

    # Insert after a specific value
    ll.insert_after_value(10, 15)
    ll.print()

    # Reverse the linked list
    ll.reverse()
    ll.print()

    # Find a value
    print("Find 15:", ll.find(15))
    print("Find 99:", ll.find(99))

    # Print length
    print("Length of linked list:", ll.length())
