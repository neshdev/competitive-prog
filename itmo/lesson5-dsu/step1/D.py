"""
Since we know that the graph will eventually will be fully disconnected
We can process the queries backwards.

For example, if the last query is an ask, then we know that we are fully disconnected
The first 'cut' will be the only connected component, in which case they should be unioned.
"""
import sys

if sys.version_info[0] < 3:
    from io import BytesIO as stream
else:
    from io import StringIO as stream

sys.stdin = stream(sys.stdin.read())
def input(): return sys.stdin.readline().rstrip('\r\n')


class DSU:
    def __init__(self, n):
        self.ps = list(range(n))
        self.ranks = [0]*n
        self.n = n

    def get(self, x):
        """
        Path compression
        """
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

        if ranks[v] > ranks[w]:
            self.ps[w] = v
        else:
            self.ps[v] = w


n, m, q = [int(x) for x in input().split()]
for _ in range(m):
    input()

queries = []
for _ in range(q):
    arr = input().split()
    queries.append(arr)

dsu = DSU(n)
out = []
for q, v, w in queries[::-1]:
    v, w = int(v)-1, int(w)-1
    if q == "ask":
        ans = "YES" if dsu.get(v) == dsu.get(w) else "NO"
        out.append(ans)
    else:
        dsu.union(v, w)

out = reversed(out)
if out:
    print("\n".join(out))
print("")