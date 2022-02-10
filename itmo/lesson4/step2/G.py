def good(arr, m, k):
    slots = m * k
    for i in range(n):
        slots -= min(m, arr[i])
    return slots <= 0

"""
4 a1 a2 a3 a4
4 b1 b2 b3 b4
4 c1 c2 c3 c4
4 d1 d2 d3 d4
4 e1 e2 e3 e4

m = 5

a1 b2 c3 d4
a2 b3 c4 e1
a3 b4 d1 e2
a4 c1 d2 e3
b1 c2 d3 e4


=========================

1 a1
2 b1 b2
3 c1 c2 c3
4 d1 d2 d3 d4
5 e1 e2 e3 e4 e5
6 f1 f2 f3 f4 f5 f6

can i make k = 4 ?

a1 b1 c1 d1
e1 f1 b2 c2
d2 e2 f2 c3
d3 e3 f3 d4
e4 f4 e5 f5
f6



"""

def binary_search(arr, k):
    """
                    L   R
k        0 1  2   3   4   5   6   7   8   9
f(k)     1 1  1   1   1   1   0   0   0   0
    
    """
    N = len(arr)
    l = 0        # f(l) <= k
    r = 10**20       # f(r) > k
    while r > l + 1:
        m = (l + r) // 2
        if good(arr, m, k):
            l = m
        else:
            r = m
    return l


MAX_STUDENTS = 50
MAX_CONSTRAINT = 20

k = int(input())
n = int(input())

arr = [0]*50
for i in range(n):
    arr[i] = int(input())

ans = binary_search(arr, k)
print(ans)