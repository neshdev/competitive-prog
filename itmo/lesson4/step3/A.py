def f(arr, t):
    # print(t)
    N = len(arr)
    x0,v0 = arr[0]
    l,r = x0 - t*v0, x0 + t*v0
    for i in range(1, N):
        xi,vi = arr[i]
        l1, r1 = xi - t*vi, xi + t*vi
        
        if l1 < l:
            (l,r), (l1,r1) = (l1,r1), (l,r)

        if l1 > r:
            return False

        l,r = max(l,l1), min(r,r1)
    return True

def binary_search(arr):
    """
    min (max (...))

    min max | x - x[i] | /v[i]

    max | x - x[i]/v[i] |  and be rewritten
        => | x - x[i]/v[i] | <= t

        min | x - x[i]/v[i] | <= t

        | x - x[i] | / v[i] <= t
        1. +(x - x[i])  <= t*v[i]   
                => x <= x[i] + t*v[i]
        2. -(x - x[i])  <= t*v[i]   
                => x - x[i] >= -t*v[i]
                => x >= x[i]   -t*v[i]

        x[i] -t*v[i] <= x <= x[i] + t*v[i]

                    L   R
    -1  0   1   2   3   4   5   6   7   8   time
    F   F   F   F   F   T   T   T   T   T   f
    
    
    """
    l = -1
    r = 10**9+1
    for i in range(60):
        t = (l + r) / 2
        if f(arr, t):
            r = t
        else:
            l = t
    # return float("{:.6f}".format(r))
    return r


n = int(input())
arr = []
for _ in range(n):
    item = [int(x) for x in input().split()]
    arr.append(item)

ans = binary_search(arr)
print(ans)