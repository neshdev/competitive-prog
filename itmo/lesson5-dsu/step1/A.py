class DSU:
    def __init__(self, n):
        self.xs = [i for i in range(n)]
        self.ranks = [0 for i in range(n)]

    def get(self, x):
        if self.xs[x] == x:
            return x
        else:
            self.xs[x] = self.get(self.xs[x])
            return self.xs[x]

    def union(self, v,w):
        v = self.get(v)
        w = self.get(w)
        if v != w:
            if self.ranks[v] == self.ranks[w]:
                self.ranks[v] += 1
            
            if self.ranks[v] > self.ranks[w]:
                self.xs[w] = v
            else:
                self.xs[v] = w
            

    


n,q = [int(x) for x in input().split()]

dsu = DSU(n)
out = [] 
for _ in range(q):
    arr = input().split()
    v,w = [int(x)-1 for x in arr[1:]]
    if arr[0] == "union":
        dsu.union(v,w)
        print(dsu.xs, dsu.ranks)
    else:
        ans = "YES" if dsu.get(v) == dsu.get(w) else "NO"
        out.append(ans)

print("\n".join(out))
        