def good(arr, x, balloons):
    total = 0
    # x_p = int(x)
    for t,z,y in arr:
        # q,r = divmod(x, (t*z+y))
        # total += q*z
        # if r >= t*z:
        #     total += z
        # else:
        #     total += (r // t)
        # print(q,r,x_p, balloons, (t,z,y), taken, x)
        T = x
        total += T // (t*z + y ) * z + min( ( T % (t*z + y )//t ) , z )
    return total >= balloons

def taken(arr, x):
    result = []
    # x_p = int(x)
    for t,z,y in arr:
        total = 0 
        # q,r = divmod(x, (t*z+y))
        # total += q*z
        # if r >= t*z:
        #     total += z
        # else:
        #     total += (r // t)
        T = x
        total += T // (t*z + y ) * z + min( ( T % (t*z + y )//t ) , z )
        result.append(total)
    return result

def binary_search(arr,balloons):
    """  
                        L   R
    -1  1   2   3   4   5   6   7   8    TIME
    F   F   F   F   F   F   T   T   T    good

    """
    l = -1
    r = 10**20
    while r > l + 1:
        m = (l + r) // 2
        if good(arr, m, balloons):
            r = m
        else:
            l = m
    return r


m,n = [int(x) for x in input().split()]
arr = []
for _ in range(n):
    test = [int(x) for x in input().split()]
    arr.append(test)

ans = binary_search(arr, m)
print(ans)
for t in taken(arr, ans):
    print(min(m,t), end=" ")
    m -= min(m,t)