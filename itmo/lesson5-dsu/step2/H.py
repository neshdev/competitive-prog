import sys

if sys.version_info[0] < 3:
    from io import BytesIO as stream
else:
    from io import StringIO as stream

sys.stdin = stream(sys.stdin.read())


def input(): return sys.stdin.readline().rstrip('\r\n')


"""
Find the MST with the highest costs nodes connected.

This will let us minimize the cost for edges for removal. 
Using a greedy approach, we take remove edges with the lowest cost.
Implicitly, this allows for us to maximize the number of edges removed.
"""

class DSU:
    def __init__(self, n):
        self.n = n
        self.parents = list(range(n))
        self.ranks = [0]*n

    def get(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.get(self.parents[x])
            return self.parents[x]

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

        self.parents[w] = v


n, q, s = [int(x) for x in input().split()]
original = []
for _ in range(q):
    arr = [int(x) for x in input().split()]
    original.append(arr)

edges = list(enumerate(original))

edges.sort(key=lambda x: x[1][2], reverse=True)
# print(edges)
dsu = DSU(n+1)

total = 0
deleted = 0
idx = []
for j, (u, v, weight) in edges:
    if dsu.get(u) != dsu.get(v):
        dsu.union(u, v)
    else:
        idx.append((j, weight))
    # print(dsu.parents)

idx.sort(key=lambda x: x[1])

deleted = 0
total = 0

# print(idx, s)
final = []
for i, weight in idx:
    if total + weight <= s:
        total += weight
        deleted += 1
        final.append(str(i+1))
    if total > s:
        break

final.sort()

print(deleted)
print(" ".join(final))
