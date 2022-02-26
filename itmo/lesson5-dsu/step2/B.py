"""
For this solution, both path compression and ranks are used.
DSU queries take O(1) = O(ackerman(n))

Using max's to find who's on the right side

This is circular dsu structure.
1. Use a virutual node for the right end.
2. If next space is the virtual node, ask 0 node for the next available spot.
   Otherwise, next space is given 


"""

class DSU:
    def __init__(self, n) -> None:
        self.n = n
        self.parents = list(range(n))
        self.ranks = [0]*n
        self.maxs = list(range(n))
        
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

        if self.ranks[v] == self.ranks[w]:
            self.ranks[v] += 1

        if self.ranks[v] < self.ranks[w]:
            v,w = w,v        

        self.parents[w] = v
        self.maxs[v] = max(self.maxs[v], self.maxs[w])
        

n = int(input())
arr = [int(x)-1 for x in input().split()]

dsu = DSU(n+1)
out = []
for v in arr:
    v = dsu.maxs[dsu.get(v)]
    # print(f"{v=}")
    if v == n:
        v = dsu.maxs[dsu.get(0)]
    out.append(v+1)
    dsu.union(v, v+1)

out = map(str, out)
print(" ".join(out))