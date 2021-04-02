import random
from binary_tree.tree import *


class DefaultTree:
    # @staticmethod
    # def try_some_functions():
    #
    #     min_range = 1
    #     max_range = 10
    #     rand = random.randint(min_range, max_range)
    #     length = 5
    #     array = random.sample(range(min_range, max_range), length)
    #     print("Generated list is: ", array)
    #     t = tree(array)
    #     print("Binary tree is: ", t.traverse())
    #     el = rand
    #     print(f"The search of element {el} in the tree: ", t.search(el))

    def __init__(self, node_count: int = 0):
        if node_count:
            array = random.sample(range(0, node_count * 3), node_count)
        else:
            array = [None]
        self.tree = tree(array)

    def get_tree(self):
        if self.tree.root.n:
            print(self.tree.traverse())

    def proof_node(self, value: int):
        if self.tree.root.n:
            if self.tree.search(value):
                return "+"
            else:
                self.add_node(value)
                return "-"
        else:
            self.add_node(value)
            return "-"

    def add_node(self, value: int):
        if not self.tree.root.n:
            self.tree = tree([value])
        else:
            self.tree.addNode(value)


class Treap:
    class Node:
        def __init__(self, value=None, priority=None):
            self.value = value
            if not priority:
                self.priority = random.randint(1, 10000)
            else:
                self.priority = priority
            self.left = None
            self.right = None

        def copy(self):
            node = Treap.Node(self.value, self.priority)
            node.left = self.left
            node.right = self.right
            return node

        def add_left(self, value, priority):
            self.left = Treap.Node(value, priority)

        def add_right(self, value, priority):
            self.right = Treap.Node(value, priority)

    @staticmethod
    def _building_tree(values, priorities):
        root = Treap.Node(priority=max(priorities))
        root.value = values[priorities.index(root.priority)]
        less_priorities = []
        less_values = []
        over_priorities = []
        over_values = []
        for i, value in enumerate(values):
            if value < root.value:
                less_priorities.append(priorities[i])
                less_values.append(value)
            elif value > root.value:
                over_priorities.append(priorities[i])
                over_values.append(value)
        if len(less_values) != 0:
            root.left = Treap._building_tree(less_values, less_priorities)
        if len(over_values) != 0:
            root.right = Treap._building_tree(over_values, over_priorities)
        return root

    @staticmethod
    def _merge(a: Node, b: Node):
        if not a or not b:
            if not a:
                return b
            else:
                return a
        if a.priority > b.priority:
            a.right = Treap._merge(a.right, b)
            return a
        else:
            b.left = Treap._merge(a, b.left)
            return b

    @staticmethod
    def _split(n: Node, key: int, a: Node, b: Node):
        if not n:
            a = b = None
            return a, b
        elif not n.value:
            a = b = None
            return a, b
        if n.value < key:
            n.right, b = Treap._split(n.right, key, n.right, b)
            return n, b
        else:
            a, n.left = Treap._split(n.left, key, a, n.left)
            return a, n

    def __init__(self, node_count: int):
        self.values = random.sample(range(0, node_count), node_count)
        self.priorities = random.sample(range(0, node_count), node_count)
        if node_count != 0:
            self.root = self._building_tree(self.values, self.priorities)
        else:
            self.root = None

    def get_treap(self):
        if not self.root:
            return None
        current_nodes = [self.root]
        output_nodes = [f"root({self.root.value}, {self.root.priority})"]
        next_nodes = []
        while len(current_nodes) != 0:
            print(''.join(output_nodes))
            output_nodes, next_nodes = [], []
            for i, current in enumerate(current_nodes):
                if current.left:
                    next_nodes.append(current.left)
                    output_nodes.append(f"l[{i}]({current.left.value}, {current.left.priority})")
                if current.right:
                    next_nodes.append(current.right)
                    output_nodes.append(f"r[{i}]({current.right.value}, {current.right.priority})")
            current_nodes = next_nodes

    def contains(self, value: int, adding: bool):
        less, equal, greater = Treap.Node(), Treap.Node(), Treap.Node()
        less, greater = Treap._split(self.root, value, less, greater)
        equal, greater = Treap._split(greater, value + 1, equal, greater)
        result = True
        if not equal:
            result = False
        self.root = Treap._merge(Treap._merge(less, equal), greater)
        if not equal and adding:
            self.insert(value=value)
        return result

    def insert(self, value: int):
        less, greater = Treap.Node(), Treap.Node()
        less, greater = Treap._split(self.root, value, less, greater)
        self.root = Treap._merge(Treap._merge(less, Treap.Node(value=value)), greater)

    def contains_next(self, value: int):
        have = "+" if self.contains(value, True) else "-"
        less, greater, equal = Treap.Node(), Treap.Node(), Treap.Node()
        less, greater = Treap._split(self.root, value, less, greater)
        equal, greater = Treap._split(greater, value + 1, equal, greater)
        next = greater.copy() if greater else None
        while next and next.left:
            next = next.left
        have_next = str(next.value) if next else "-"
        self.root = Treap._merge(Treap._merge(less, equal), greater)
        return have + ' ' + str(have_next)