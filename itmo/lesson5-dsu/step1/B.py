import sys

if sys.version_info[0] < 3:
    from io import BytesIO as stream
else:
    from io import StringIO as stream

sys.stdin = stream(sys.stdin.read())
def input(): return sys.stdin.readline().rstrip('\r\n')


class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.ranks = [0]*n
        self.maxs = list(range(n))
        self.mins = list(range(n))
        self.counts = [1]*n

    def get(self, x):
        if self.p[x] == x:
            return x
        else:
            self.p[x] = self.get(self.p[x])
            return self.p[x]

    def union(self, v, w):
        v = self.get(v)
        w = self.get(w)

        if v == w:
            return

        if self.ranks[v] == self.ranks[w]:
            self.ranks[v] += 1

        if self.ranks[v] > self.ranks[w]:
            self.p[w] = v
            self.maxs[v] = max(self.maxs[v], self.maxs[w])
            self.mins[v] = min(self.mins[v], self.mins[w])
            self.counts[v] += self.counts[w]
        else:
            self.p[v] = w
            self.maxs[w] = max(self.maxs[v], self.maxs[w])
            self.mins[w] = min(self.mins[v], self.mins[w])
            self.counts[w] += self.counts[v]


n, q = [int(x) for x in input().split()]

dsu = DSU(n)
out = []
for _ in range(q):
    arr = input().split()
    if arr[0] == "union":
        v, w = [int(x)-1 for x in arr[1:]]
        dsu.union(v, w)
    else:
        w = int(arr[1])-1
        w1 = dsu.get(w)
        ans = f"{dsu.mins[w1]+1} {dsu.maxs[w1]+1} {dsu.counts[w1]}"
        out.append(ans)

print("\n".join(out))
