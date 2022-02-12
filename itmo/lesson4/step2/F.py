"""
N = len(s)

binary_search = O (log N) = log N

good = O(2*N)

total time = O* ( 2*N log N ) = N log N
"""

def good(s, p, arr, m):
    N = len(arr)
    s = list(s)
    for i in range(0, m):
        s[arr[i]-1] = None
    
    i = 0
    for j in range(N):
        if s[j] and s[j] == p[i]:
            i += 1
        if i == len(p):
            break
    # print(m,s,i)
    return i == len(p)

def binary_search(s,p,arr):
    """
                L   R
    -1  0   1   2   3   4   5   6   7   
    T   T   T   T   F   F   F   F   F
    
    """
    l = -1
    r = len(arr)
    while r > l + 1:
        m = (l + r) // 2
        if good(s,p,arr,m):
            l = m
        else:
            r = m
    return 0 if l == -1 else l


s = input()
p = list(input())
arr = [int(x) for x in input().split()]
ans = binary_search(s,p,arr)
print(ans)