# Tree Data Structure Overview
#
# A tree is a widely used data structure in computer science that simulates a hierarchical tree structure,
# with a root value and subtrees of children, represented as a set of linked nodes. Each node contains a value
# or data and references to its child nodes and, optionally, its parent node. Trees are used to represent
# hierarchical relationships, such as organizational structures, file systems, or geographical locations.
#
# Key Terminology:
# - Root: The topmost node in the tree, which has no parent.
# - Parent: A node that has child nodes.
# - Child: A node that is a descendant of another node.
# - Leaf: A node with no children.
# - Level: The depth of a node in the tree, starting from 0 at the root.
# - Subtree: A tree consisting of a node and its descendants.
#
# Applications:
# - File systems
# - Organizational structures
# - Decision trees in machine learning
# - XML/HTML document object models (DOM)
# - Trie for string operations (e.g., autocomplete)


class TreeNode:
    def __init__(self, data):
        """Initialize a tree node with data, children, and a parent."""
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        """Add a child node to the current node."""
        child.parent = self
        self.children.append(child)

    def get_level(self):
        """Calculate the level (depth) of the current node."""
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        """Print the tree structure starting from the current node."""
        prefix = " " * self.get_level() * 3 + "|__" if self.parent else ""
        print(prefix + self.data)
        for child in self.children:
            child.print_tree()


def build_product_tree():
    """Build and display a tree representing product categories."""
    root = TreeNode("Electronics")

    # Adding categories and products
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    # Adding categories to the root
    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()


class HierarchyTreeNode:
    def __init__(self, name, designation):
        """Initialize a tree node with a name, designation, children, and a parent."""
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self, child):
        """Add a child node to the current node."""
        child.parent = self
        self.children.append(child)

    def get_level(self):
        """Calculate the level (depth) of the current node."""
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, print_type):
        """Print the tree structure based on the specified print type."""
        prefix = " " * self.get_level() * 3 + "|__" if self.parent else ""
        if print_type == "name":
            print(prefix + self.name)
        elif print_type == "designation":
            print(prefix + self.designation)
        else:
            print(f"{prefix}{self.name} ({self.designation})")

        for child in self.children:
            child.print_tree(print_type)


def build_management_tree():
    """Build and return a tree representing a company hierarchy."""
    # CTO Hierarchy
    infra_head = HierarchyTreeNode("Vishwa", "Infrastructure Head")
    infra_head.add_child(HierarchyTreeNode("Dhaval", "Cloud Manager"))
    infra_head.add_child(HierarchyTreeNode("Abhijit", "App Manager"))

    cto = HierarchyTreeNode("Chinmay", "CTO")
    cto.add_child(infra_head)
    cto.add_child(HierarchyTreeNode("Aamir", "Application Head"))

    # HR hierarchy
    hr_head = HierarchyTreeNode("Gels", "HR Head")
    hr_head.add_child(HierarchyTreeNode("Peter", "Recruitment Manager"))
    hr_head.add_child(HierarchyTreeNode("Waqas", "Policy Manager"))

    # CEO node
    ceo = HierarchyTreeNode("Nilupul", "CEO")
    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo


class LocationTreeNode(TreeNode):
    def print_tree(self, depth):
        """Print the tree structure up to the specified depth."""
        if self.get_level() <= depth:
            prefix = " " * self.get_level() * 3 + "|__" if self.parent else ""
            print(prefix + self.data)
        for child in self.children:
            child.print_tree(depth)


def build_location_tree():
    """Build and return a tree representing geographical locations."""
    root = LocationTreeNode("Global")

    india = LocationTreeNode("India")
    gujarat = LocationTreeNode("Gujarat")
    gujarat.add_child(LocationTreeNode("Ahmedabad"))
    gujarat.add_child(LocationTreeNode("Baroda"))

    karnataka = LocationTreeNode("Karnataka")
    karnataka.add_child(LocationTreeNode("Bangluru"))
    karnataka.add_child(LocationTreeNode("Mysore"))

    india.add_child(gujarat)
    india.add_child(karnataka)

    usa = LocationTreeNode("USA")
    nj = LocationTreeNode("New Jersey")
    nj.add_child(LocationTreeNode("Princeton"))
    nj.add_child(LocationTreeNode("Trenton"))

    california = LocationTreeNode("California")
    california.add_child(LocationTreeNode("San Francisco"))
    california.add_child(LocationTreeNode("Mountain View"))
    california.add_child(LocationTreeNode("Palo Alto"))

    usa.add_child(nj)
    usa.add_child(california)

    root.add_child(india)
    root.add_child(usa)

    return root


if __name__ == "__main__":
    # Build and display product tree
    build_product_tree()

    # Build and display management tree
    management_tree = build_management_tree()
    management_tree.print_tree("name")
    management_tree.print_tree("designation")
    management_tree.print_tree("both")

    # Build and display location tree
    location_tree = build_location_tree()
    location_tree.print_tree(1)
    location_tree.print_tree(2)
    location_tree.print_tree(3)
