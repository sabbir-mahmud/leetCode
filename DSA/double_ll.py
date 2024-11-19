class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
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

        itr.next = Node(data, itr)
        return

    def insert_at_beg(self, data):
        if self.head is None:
            self.head = Node(data)

        itr = self.head
        node = Node(data, None, itr)
        itr.prev = node
        self.head = node
        return

    def insert_values(self, values: list):
        for i in values:
            print(i)
            self.insert(i)
        return

    def get_last_node(self):
        itr = self.head

        while itr.next:
            itr = itr.next

        return itr

    def print_forward(self):
        ll = ""
        itr = self.head

        while itr:
            ll += f"{itr.data} --> "
            itr = itr.next
        print(ll)
        return

    def print_backward(self):
        ll = ""
        itr = self.get_last_node()

        while itr:
            ll += f"{itr.data} --> "
            itr = itr.prev
        print(ll)
        return


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_beg("apple")
    ll.print_forward()
    ll.print_backward()
