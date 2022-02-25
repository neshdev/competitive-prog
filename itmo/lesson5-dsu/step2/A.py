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
        self.maxs = list(range(n))
        self.n = n

    def get(self, x):
        if self.ps[x] == x:
            return x
        else:
            self.ps[x] = self.get(self.ps[x])
            return self.ps[x]

    def union(self, l, r):
        v = self.get(l)
        w = self.get(r)
        if v == w:
            return
        # print(f"{v=},{w=}")
        if self.ranks[v] == self.ranks[w]:
            self.ranks[w] += 1

        if self.ranks[v] > self.ranks[w]:
            self.ps[w] = v
            self.maxs[v] = max(self.maxs[v], self.maxs[w])
        else:
            self.ps[v] = w
            self.maxs[w] = max(self.maxs[v], self.maxs[w])

            


n, q = [int(x) for x in input().split()]
dsu = DSU(n+2)

out = []
for _ in range(q):
    arr = input().split()
    idx = int(arr[1])
    if arr[0] == "?":
        # print(arr)
        ans = dsu.maxs[dsu.get(idx)]
        if ans == n+1:
            ans = -1
        out.append(ans)
        # print(ans, dsu.maxs, dsu.ranks, dsu.ps)
    else:
        # print("rem", arr, idx, idx+1)
        dsu.union(idx, idx+1)

out = map(str, out)
print("\n".join(out))
print()
