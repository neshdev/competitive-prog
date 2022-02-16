"""
ex1:

k=4
1 3
5 7
   0 1 2 3 4 5
| [1 2 3 5 6 7] | 
a[k] = a[4] = 6
"""



"""
ex2:

k=3
1 4 
3 5

0 1 2 3 4 5 6
1 2 3 3 4 4 5
a[k] = a[3] = 3

"""
def cnt(arr, m, k):
    count = 0
    for lo,hi in arr:
        if lo <= m <= hi:
            count += m-lo+1
        elif hi < m:
            count += hi-lo+1
    return count >= k

def binary_search(arr, k):
    l = -10**10-1   # cnt(l) <   k
    r = 10**10    # cnt(r) >=  k
    while r > l + 1:
        m = (l + r) // 2
        if cnt(arr, m, k):
            r = m
        else:
            l = m
    return r


n,k = [int(x) for x in input().split()]

arr = []
for _ in range(n):
    item = [int(x) for x in input().split()]
    arr.append(item)

ans = binary_search(arr, k+1)
print(ans)