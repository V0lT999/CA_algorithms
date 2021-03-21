import random
from binary_tree.tree import *


class DefaultTree:
    @staticmethod
    def try_some_functions():

        min_range = 1
        max_range = 10
        rand = random.randint(min_range, max_range)
        length = 5
        array = random.sample(range(min_range, max_range), length)
        print("Generated list is: ", array)
        t = tree(array)
        print("Binary tree is: ", t.traverse())
        el = rand
        print(f"The search of element {el} in the tree: ", t.search(el))


class Treap:
    class Node:
        def __init__(self, value=0, priority=0):
            self.value = value
            self.priority = priority
            self.left = None
            self.right = None

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

    def __init__(self, node_count):
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
