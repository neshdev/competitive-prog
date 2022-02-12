from collections import deque

class Graph:
    def __init__(self, n) -> None:
        self.nodes = [[] for i in range(n+1)]
        self.n = n

    def add_edge(self, v, w, weight):
        self.nodes[v].append((w, weight))

    def adj_to(self, v):
        return self.nodes[v]

class Cons:
    def __init__(self, head, tail=None) -> None:
        self.head = head
        self.tail = tail
        
    def __repr__(self) -> str:
        node = self
        out = []
        while node:
            out.append(node.head)
            node = node.tail
        return ":".join(list(map(str, out))) + "[]"

    def length(self):
        node = self
        count = 0
        while node:
            count += 1
            node = node.tail
        return count

    def reverse(self):
        path = None
        node = self
        while node:
            path = Cons(node.head, path)
            node = node.tail
        return path

def search(g: Graph, max_weight, d):
    reachable = False
    goal = g.n
    q = deque([(1,d, Cons(1))])
    while q:
        v, edge_limit, path = q.popleft()
        if v == goal:
            reachable = True
            break
        
        if edge_limit > 0:
            for w, weight in g.adj_to(v):
                if weight <= max_weight:
                    item = w, edge_limit-1, Cons(w,path)
                    q.append(item)
    # print("final", max_weight, path, path.length(), reachable and path.length()-1 <= d)
    return reachable and path.length()-1 <= d, path
            


def good(g, m, d):
    return  search(g, m, d)[0]

def binary_search(g, d):
    """
    L   R
    -1  0   1   2   3   4   5   6
    F   F   F   T   T   T   T   T
    
    """
    l = -1
    r = 10**9+1
    # r = 100
    while r > l + 1:
        m = (l + r) // 2
        if good(g, m, d):
            r = m
        else:
            l = m
    return r




n,m,d = [int(x) for x in input().split()]
g = Graph(n)


for _ in range(m):
    v,w,weight = [int(x) for x in input().split()]
    g.add_edge(v,w,weight)


min_edge_weight = binary_search(g, d)

reachable, path = search(g, min_edge_weight, d)
if reachable:
    path = path.reverse()
    print(path.length()-1)
    while path:
        print(path.head, end=" ")
        path = path.tail
else:
    print("-1")