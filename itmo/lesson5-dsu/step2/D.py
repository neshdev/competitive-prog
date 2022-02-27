import sys

if sys.version_info[0] < 3:
    from io import BytesIO as stream
else:
    from io import StringIO as stream

sys.stdin = stream(sys.stdin.read())
def input(): return sys.stdin.readline().rstrip('\r\n')


class DSU:
    def __init__(self, n) -> None:
        self.n = n
        self.parents = list(range(n))
        self.distances = [0]*n

    def get(self, x):
        if self.parents[x] == x:
            return x
        else:
            root = self.get(self.parents[x])
            self.distances[x] += self.distances[self.parents[x]]
            self.parents[x] = root
            return root

    def union(self, v, w):
        v = self.get(v)
        w = self.get(w)
        if v == w:
            return

        self.parents[v] = w
        self.distances[v] += self.distances[w]+1

    def depth(self, x):
        if self.parents[x] == x:
            return self.distances[x]
        else:
            result = self.distances[x] + self.depth(self.parents[x])
            return result


n, q = [int(x) for x in input().split()]

dsu = DSU(n+1)

out = []
for _ in range(q):
    arr = [int(x) for x in input().split()]
    if arr[0] == 1:
        v, w = arr[1:]
        dsu.union(v, w)
    else:
        c = arr[1]
        dsu.get(c)
        ans = dsu.depth(c)
        # print(dsu.distances,arr)
        out.append(ans)

out = map(str, out)
print("\n".join(out))
