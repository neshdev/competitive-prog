import sys

if sys.version_info[0] < 3:
    from io import BytesIO as stream
else:
    from io import StringIO as stream

sys.stdin = stream(sys.stdin.read())
def input(): return sys.stdin.readline().rstrip('\r\n')

"""
You need 2 DSU's, main and auxilary

Main is for checking if you are connected to any two components
Auxilary if for connecting ranges.
Auxilary can connect ranges very quickly -> you can use the "parking" lot trick.
As you are merging components, you update the Main DSU

Queries are only on simplified DSU

Runtime Analysis
==============================
N nodes
Q queries

ackerman(n) ~ 1

O(Q * ackerman(n)) = O(Q + N)

Spacetime Analysis:
DSU
====
C = 1 for mins, 1 for max, 1 for parents, 1 for parents
O(n * C) = O(n)
"""

class DSU:
    def __init__(self, n) -> None:
        self.n = n
        self.parents = list(range(n))
        self.ranks = [0]*n
        self.maxs = list(range(n))
        self.mins = list(range(n))

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
        self.maxs[v] = max(self.maxs[v], self.maxs[w])
        self.mins[v] = min(self.mins[v], self.mins[w])


n, q = [int(x) for x in input().split()]

range_dsu = DSU(n+1)
single_dsu = DSU(n+1)

out = []
for _ in range(q):
    arr = [int(x) for x in input().split()]
    v, w = [x for x in arr[1:]]
    if arr[0] == 3:
        if single_dsu.get(v) == single_dsu.get(w):
            out.append("YES")
        else:
            out.append("NO")
    elif arr[0] == 2:
        v = range_dsu.maxs[range_dsu.get(v)]
        while v < w:
            range_dsu.union(v, min(v+1, n))
            single_dsu.union(v, min(v+1, n))
            v = range_dsu.maxs[range_dsu.get(v)]
    else:
        single_dsu.union(v, w)

print("\n".join(out))
