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
        self.data = data  # Value of the node
        self.left = None  # Left child (stores smaller values)
        self.right = None  # Right child (stores larger values)

    def add_child(self, data):
        """
        Add a child node to the BST, ensuring the BST property is maintained.
        :param data: Value to be added.
        """
        if self.data == data:
            # Ignore duplicate values
            return

        if data < self.data:
            # If data is smaller, add to the left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # If data is larger, add to the right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, value):
        """
        Search for a value in the BST.
        :param value: Value to search for.
        :return: True if found, False otherwise.
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
        Perform an in-order traversal of the tree.
        :return: Sorted list of elements in ascending order.
        """
        elements = []
        # Visit left subtree
        if self.left:
            elements += self.left.in_order_traversal()
        # Visit root node
        elements.append(self.data)
        # Visit right subtree
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def post_order_traversal(self):
        """
        Perform a post-order traversal of the tree.
        :return: List of elements in post-order (left, right, root).
        """
        elements = []
        # Visit left subtree
        if self.left:
            elements += self.left.post_order_traversal()
        # Visit right subtree
        if self.right:
            elements += self.right.post_order_traversal()
        # Visit root node
        elements.append(self.data)
        return elements

    def pre_order_traversal(self):
        """
        Perform a pre-order traversal of the tree.
        :return: List of elements in pre-order (root, left, right).
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
        Find the smallest value in the BST.
        :return: Minimum value in the tree.
        """
        return self.left.find_min() if self.left else self.data

    def find_max(self):
        """
        Find the largest value in the BST.
        :return: Maximum value in the tree.
        """
        return self.right.find_max() if self.right else self.data

    def calculate_sum(self):
        """
        Calculate the sum of all node values in the BST.
        :return: Total sum of all elements.
        """
        return sum(self.in_order_traversal())

    def delete(self, val):
        """
        Delete a node from the BST while maintaining its properties.
        :param val: Value to be deleted.
        :return: Updated subtree after deletion.
        """
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            # Node with no children
            if self.left is None and self.right is None:
                return None

            # Node with one child
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            # Node with two children: Replace with in-order successor
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self


def build_tree(elements):
    """
    Build a binary search tree from a list of elements.
    :param elements: List of elements to insert into the BST.
    :return: Root node of the constructed BST.
    """
    root = BinarySearchTreeNode(elements[0])
    for element in elements[1:]:
        root.add_child(element)
    return root


if __name__ == "__main__":
    # Example 1: Using a list of strings (countries)
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
    numbers_tree.delete(1)
    numbers_tree.delete(34)
    print("In-order traversal after deletions:", numbers_tree.in_order_traversal())
