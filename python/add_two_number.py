from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        """
        Initializes a node with a given value and a pointer to the next node.
        :param val: Integer value of the node.
        :param next: Pointer to the next ListNode in the linked list.
        """
        self.val = val
        self.next = next

    def __str__(self):
        """
        Returns a string representation of the linked list for easy visualization.
        """
        result = []
        node = self
        while node:
            result.append(str(node.val))
            node = node.next
        return " -> ".join(result)


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Adds two numbers represented as linked lists and returns the sum as a new linked list.
        Each node contains a single digit, and digits are stored in reverse order.

        :param l1: Head of the first linked list.
        :param l2: Head of the second linked list.
        :return: Head of the resulting linked list representing the sum.

        Time Complexity: O(max(N, M)) - We iterate through the longest list.
        Space Complexity: O(max(N, M)) - We store the result in a new linked list.
        """
        dummy = ListNode(0)  # Dummy node to simplify list construction
        current = dummy  # Pointer to track the last node in the result list
        carry = 0  # Carry for addition

        # Traverse both lists while there are remaining digits or a carry exists
        while l1 or l2 or carry:
            if l1:
                carry += l1.val  # Add l1's value to carry
                l1 = l1.next  # Move to the next node in l1

            if l2:
                carry += l2.val  # Add l2's value to carry
                l2 = l2.next  # Move to the next node in l2

            current.next = ListNode(
                carry % 10
            )  # Create new node with digit value (carry mod 10)
            current = current.next  # Move pointer forward
            carry //= 10  # Update carry for the next iteration

        return dummy.next  # Return the head of the resulting linked list


if __name__ == "__main__":

    def create_linked_list(values):
        """
        Creates a linked list from a list of values.
        :param values: List of integers.
        :return: Head of the linked list.
        """
        if not values:
            return None
        head = ListNode(values[0])  # Initialize head
        current = head  # Pointer to track the last node
        for val in values[1:]:
            current.next = ListNode(val)  # Create and link new node
            current = current.next  # Move pointer forward
        return head

    # Example test case
    l1 = create_linked_list([2, 4, 3])  # Represents number 342
    l2 = create_linked_list([5, 6, 4])  # Represents number 465

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    # Print result
    print("Result:", result)
