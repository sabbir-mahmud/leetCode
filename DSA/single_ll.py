class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data)
        return

    def insert_at_beg(self, data):
        self.head = Node(data, self.head)
        return

    def insert_values(self, data: list):
        for i in data:
            self.insert(i)
        return

    def insert_after_value(self, value, data):
        itr = self.head

        while itr:
            print(itr.data)
            if itr.data == value:
                break
            itr = itr.next

        itr.next = Node(data, itr.next)
        return

    def remove_at_end(self):
        itr = self.head
        prev = None

        while itr.next:
            prev = itr
            itr = itr.next

        prev.next = None

        return

    def remove_by_value(self, value):
        itr = self.head
        prev = None

        while itr:
            if itr.data == value:
                break
            prev = itr
            itr = itr.next

        prev.next = itr.next
        return

    def print(self):
        ll = ""
        itr = self.head

        while itr:
            ll += f"{itr.data} --> "
            itr = itr.next
        print(ll)


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.insert_at_beg("cow")
    ll.insert_after_value("mango", "apple")  # insert apple after mango
    ll.print()
    ll.remove_by_value("orange")  # remove orange from linked list
    ll.print()
