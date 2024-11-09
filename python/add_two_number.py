from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Helper function to print the linked list.
    def __str__(self):
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
        ptr = ListNode(0)
        s = ptr
        c = 0

        while l1 or l2 or c:
            if l1:
                c += l1.val
                l1 = l1.next

            if l2:
                c += l2.val
                l2 = l2.next

            ptr.next = ListNode(c % 10)
            ptr = ptr.next
            c //= 10
        return s.next


if __name__ == "__main__":

    def create_linked_list(values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    # Test case
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    # Print result
    print("Result:", result)
