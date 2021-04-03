import random


class DSU:

    def __init__(self, n: int = 1):
        self.roots = [i for i in range(n)]

    def find(self, x: int):
        if self.roots[x] == x:
            return x
        else:
            self.roots[x] = self.find(self.roots[x])
            return self.roots[x]

    def unite(self, x: int, y: int):
        x = self.find(x)
        y = self.find(y)
        if random.randint(0, 100) % 2:
            x, y = y, x
        self.roots[x] = y

    def is_one_subset(self, x: int, y: int):
        if self.find(x) == self.find(y):
            return "YES"
        else:
            self.unite(x, y)
            return "NO"



