import sys

if sys.version_info[0] < 3:
    from io import BytesIO as stream
else:
    from io import StringIO as stream

sys.stdin = stream(sys.stdin.read())


def input(): return sys.stdin.readline().rstrip('\r\n')


class DSU:
    def __init__(self, n):
        self.n = n
        self.parents = list(range(n))
        self.ranks = [0]*n
        self.maximums = [float('-inf')]*n

    def get(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.get(self.parents[x])
            return self.parents[x]

    def union(self, v, w, weight):
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
        self.maximums[v] = max(self.maximums[v], self.maximums[w], weight)


n, q = [int(x) for x in input().split()]
edges = []
for _ in range(q):
    arr = [int(x) for x in input().split()]
    edges.append(arr)

edges.sort(key=lambda x: x[2])

dsu = DSU(n+1)
best = float("-inf")
for u, v, w in edges:
    if dsu.get(u) != dsu.get(v):
        dsu.union(u, v, w)
        best = max(best, w)

ans = dsu.maximums[dsu.get(1)]
print(ans)
