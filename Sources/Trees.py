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