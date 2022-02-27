import sys

if sys.version_info[0] < 3:
    from io import BytesIO as stream
else:
    from io import StringIO as stream

sys.stdin = stream(sys.stdin.read())


def input(): return sys.stdin.readline().rstrip('\r\n')

"""
solution is quadratic. It might be possible to do something like sliding window
"""

class DSU:
    def __init__(self, n):
        self.n = n
        self.cc = n
        self.parents = list(range(n))
        self.ranks = [0]*n
        self.minimums = [float("inf")]*n
        self.maximums = [float("-inf")]*n

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

        if self.ranks[v] < self.ranks[w]:
            v, w = w, v

        self.ranks[v] += 1
        self.parents[w] = v
        self.cc -= 1
        self.maximums[v] = max(self.maximums[v], self.maximums[w], weight)
        self.minimums[v] = min(self.minimums[v], self.minimums[w], weight)


n, q = [int(x) for x in input().split()]
edges = []
for _ in range(q):
    arr = [int(x) for x in input().split()]
    edges.append(arr)


edges.sort(key=lambda x: x[2])

best = float("inf")
possible = False
N = len(edges)
for i in range(N):
    dsu = DSU(n+1)
    for j in range(i,N):
        # print(i,j)
        u,v,w = edges[j]
        if dsu.get(u) != dsu.get(v):
            dsu.union(u,v,w)
    
        if dsu.cc == 2:
            # print((i,j))
            possible = True
            lo = dsu.minimums[dsu.get(1)]
            hi = dsu.maximums[dsu.get(1)]
            best = min(best, hi - lo)
            break

if possible:
    print("YES")
    print(best)
else:
    print("NO")


