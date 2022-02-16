def count(n, m, k):
    cnt = 0
    for i in range(1, n+1):
        cnt += min(m//i, n)
    return cnt <= k

def binary_search(n, k):
    """    
    """
    l = -1             # count(l) <= k
    r = n*n+1          # count(r) >  k
    while r > l + 1:
        m = (l + r ) // 2
        if count(n, m, k):
            l = m
        else:
            r = m
    return r


n, k = [int(x) for x in input().split()]
ans = binary_search(n, k-1)
print(ans)


def test():
    import random
    # N = random.randint(1,100)
    N = random.randint(1,10)
    arr1 = [i+1 for i in range(N)]
    arr2 = [i+1 for i in range(N)]

    expected = []
    for x in arr1:
        for y in arr2:
            expected.append(x*y)
    expected.sort()


    for k in range(N*N):
        r = binary_search(N,k)
        if r != expected[k]:
            raise Exception(f"not equal at {k} L={l}, r={r}", (l,r), expected[k], arr1, arr2, expected)
        else:
            print(f"working for index={k} {r}=={expected[k]}, {expected}")

# test()

"""
runtime analysis:

binary_search : log(Ans)
count         : N
======================
log(Ans)*N

"""