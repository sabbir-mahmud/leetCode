"""
Binary Search Tree Implementation in Python
-------------------------------------------

This script implements a Binary Search Tree (BST) with several features:
1. **Node Initialization**: Each node stores a value and pointers to left and right children.
2. **Adding Nodes**: Nodes can be added while maintaining the BST property (left child < root < right child).
3. **Search Functionality**: Efficiently searches for a value in the tree.
4. **Traversal Methods**:
   - **In-order Traversal**: Returns a sorted list of elements.
   - **Post-order Traversal**: Processes the left subtree, right subtree, and root.
   - **Pre-order Traversal**: Processes the root, left subtree, and right subtree.
5. **Find Minimum and Maximum**: Retrieves the smallest and largest values in the tree.
6. **Sum Calculation**: Computes the sum of all node values in the tree.

Utility:
- A `build_tree` function is provided to create a BST from a list of elements.
- Duplicate values are ignored to maintain the BST structure.

Example Usage:
- Build a tree from a list of numbers or strings.
- Perform various operations like searching, traversing, and finding min/max values.

Test Cases:
- A predefined set of test cases demonstrates the usage of the BST with both numeric and string data.

"""


class BinarySearchTreeNode:
    def __init__(self, data):
        """
        Initialize a Binary Search Tree node.
        :param data: Value to store in the node.
        """
        self.data = data  # Node value
        self.left = None  # Left child (smaller values)
        self.right = None  # Right child (larger values)

    def add_child(self, data):
        """
        Add a child node to the tree.
        :param data: Value to be added.
        """
        if self.data == data:  # Ignore duplicate values
            return

        if data < self.data:
            # Go to the left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)  # Create a new left child
        else:
            # Go to the right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)  # Create a new right child

    def search(self, value):
        """
        Search for a value in the tree.
        :param value: Value to search for.
        :return: True if found, else False.
        """
        if self.data == value:
            return True

        if value < self.data:
            # Search in the left subtree
            return self.left.search(value) if self.left else False
        else:
            # Search in the right subtree
            return self.right.search(value) if self.right else False

    def in_order_traversal(self):
        """
        Perform in-order traversal of the tree.
        :return: Sorted list of elements.
        """
        elements = []
        # Visit left subtree
        if self.left:
            elements += self.left.in_order_traversal()
        # Visit root
        elements.append(self.data)
        # Visit right subtree
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def post_order_traversal(self):
        """
        Perform post-order traversal of the tree.
        :return: List of elements in post-order.
        """
        elements = []
        # Visit left subtree
        if self.left:
            elements += self.left.post_order_traversal()
        # Visit right subtree
        if self.right:
            elements += self.right.post_order_traversal()
        # Visit root
        elements.append(self.data)
        return elements

    def pre_order_traversal(self):
        """
        Perform pre-order traversal of the tree.
        :return: List of elements in pre-order.
        """
        elements = [self.data]
        # Visit left subtree
        if self.left:
            elements += self.left.pre_order_traversal()
        # Visit right subtree
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

    def find_min(self):
        """
        Find the minimum value in the tree.
        :return: Minimum value.
        """
        return self.left.find_min() if self.left else self.data

    def find_max(self):
        """
        Find the maximum value in the tree.
        :return: Maximum value.
        """
        return self.right.find_max() if self.right else self.data

    def calculate_sum(self):
        """
        Calculate the sum of all values in the tree.
        :return: Sum of all elements.
        """
        return sum(self.in_order_traversal())


def build_tree(elements):
    """
    Build a binary search tree from a list of elements.
    :param elements: List of elements to add to the tree.
    :return: Root node of the binary search tree.
    """
    root = BinarySearchTreeNode(elements[0])
    for element in elements[1:]:
        root.add_child(element)
    return root


if __name__ == "__main__":
    # Example 1: Using a list of countries
    countries = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK", "USA"]
    country_tree = build_tree(countries)

    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))

    # Example 2: Using a list of numbers
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In-order traversal (sorted list):", numbers_tree.in_order_traversal())
    print("Post-order traversal:", numbers_tree.post_order_traversal())
    print("Pre-order traversal:", numbers_tree.pre_order_traversal())
    print("Min value:", numbers_tree.find_min())
    print("Max value:", numbers_tree.find_max())
    print("Sum of all values:", numbers_tree.calculate_sum())
