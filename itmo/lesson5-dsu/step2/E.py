import sys

if sys.version_info[0] < 3:
    from io import BytesIO as stream
else:
    from io import StringIO as stream

sys.stdin = stream(sys.stdin.read())


def input(): return sys.stdin.readline().rstrip('\r\n')

"""
basic MST algorithm as covered in lecture
"""

class DSU:
    def __init__(self, n):
        self.n = n
        self.ps = list(range(n))
        self.ranks = [0]*n

    def get(self, x):
        if self.ps[x] == x:
            return x
        else:
            self.ps[x] = self.get(self.ps[x])
            return self.ps[x]

    def union(self, v, w):
        v = self.get(v)
        w = self.get(w)
        if v == w:
            return

        ranks = self.ranks
        if ranks[v] == ranks[w]:
            ranks[v] += 1

        if ranks[v] < ranks[w]:
            v, w = w, v

        self.ps[w] = v


n, m = [int(x) for x in input().split()]

edges = []
for _ in range(m):
    arr = [int(x) for x in input().split()]
    edges.append(arr)


edges.sort(key=lambda x: x[2])

dsu = DSU(n)
min_weight = 0
for u, v, w in edges:
    u -= 1
    v -= 1
    if dsu.get(u) != dsu.get(v):
        dsu.union(u, v)
        min_weight += w

print(min_weight)
