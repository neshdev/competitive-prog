from collections import defaultdict

class Graph:
    def __init__(self, n) -> None:
        self.xs = defaultdict(list)
        # self.weights = {}

    def add_edge(self,u,v,w):
        self.xs[u].append((v,w))
        self.xs[v].append((u,w))
        
    def adj_to(self, v):
        return self.xs[v]


def ority(g):
    max = 10**9
    bit = 0
    while max:
        max >>= 1
        bit += 1

    ans = 2**(bit) - 1

    for k in range(bit)[::-1]:
        ans ^= 1 << k
        # print("shifting",  format(ans, "40b"))
        visited = set()
        dfs(g, 1, visited, ans)
        if not all_visited(g, visited):
            ans ^= 1 << k
    return ans



def all_visited(g, visited):
    for k in g.xs.keys():
        if k not in visited:
            return False
    return True

def dfs(g, start, visited, ans):
    q = [start]
    while q:
        u = q.pop()
        if u not in visited:
            visited.add(u)
            for v,w in g.adj_to(u):
                if ans | w == ans:
                    q.append(v)
                    



t = int(input())
for _ in range(t):
    _ = input()
    n,m = [int(x) for x in input().split()]

    g = Graph(n)

    for e in range(m):
        u,v,w = [int(x) for x in input().split()]
        g.add_edge(u,v,w)

    ans = ority(g)
    print(ans)