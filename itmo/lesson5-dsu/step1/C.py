
"""
Help from blog post: https://codeforces.com/blog/entry/96217

Idea is to not use path compression

1. Worst case when not using path compression is O(log N)

Leader will always have accumulated team score.
Child will always subtract from leader when joining.
To get final score. Go from child to root and accumulate all score.

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
        self.points = [0]*n
        self.n = n

    def get(self, x):
        if self.ps[x] == x:
            return x
        else:
            return  self.get(self.ps[x])
            # return self.ps[x]

    def union(self, v, w):
        v = self.get(v)
        w = self.get(w)
        # print("start", self.points)
        if v == w:
            return
        ranks = self.ranks
        if ranks[v] == ranks[w]:
            ranks[v] += 1

        if ranks[v] > ranks[w]:
            self.ps[w] = v
            self.points[w] -= self.points[v]
        else:
            self.ps[v] = w
            self.points[v] -= self.points[w]
        # print("end", self.points)

    def add(self,v, score):
        v = self.get(v)
        self.points[v] += score 
        # print("add", self.points)

    def accumulate(self, v):
        if self.ps[v] == v:
            return self.points[v]
        else:
            return self.points[v] + self.accumulate(self.ps[v])


n, q = [int(x) for x in input().split()]
dsu = DSU(n)

out = []

for _ in range(q):
    arr = input().split()
    # print(arr)
    if arr[0] == "add":
        v, score = [int(x) for x in arr[1:]]
        dsu.add(v-1, score)
    elif arr[0] == "join":
        v, w = [int(x) for x in arr[1:]]
        dsu.union(v-1,w-1) 
    else:
        v = int(arr[1])-1
        ans = dsu.accumulate(v)
        out.append(ans)
        # print(ans)

out = map(str, out)
print("\n".join(out))
