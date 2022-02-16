def bisect_left(arr, scalar, x):
    """
                        L   R
        0   1   2   3   3   6   7   9   10
        T   T   T   T   T   F   F   F   F   
    """
    l = -1            # f(l) <= m
    r = len(arr)      # f(r) >  m
    while r > l + 1:
        m = (l + r) // 2
        if arr[m]+scalar <= x:
            l = m
        else:
            r = m
    return  l, r

def bisect_right(arr, scalar, x):
    """
                L   R
        0   1   2   3   3   6   7   9   10
        F   F   F   T   T   T   T   T   T   
    """
    l = 0           # f(l) <  m
    r = len(arr)    # f(r) >= m
    while r > l + 1:
        m = (l + r) // 2
        if (arr[m]+scalar) >= x:
            r = m
        else:
            l = m
    return l,r


def count(arr1, arr2, m, k):
    cnt = 0
    # print("counting", m)
    for i,s in enumerate(arr2):
        
        l, r = bisect_left(arr1, s, m)
        # print(i, r, arr2[i], arr1[r]+arr2[i])
        cnt += r
    return cnt <= k


def binary_search(arr1, arr2, k):
    """
                2	4	4	6	8

        1	    3	5	5	7	9
        3	    5	7	7	9	11
        5	    7	9	9	11	13
        7	    9	11	11	13	15
        9	    11	13	13	15	17

    
    """
    l = -1             # count(l) <= k
    r = 10**10         # count(r) >  k
    while r > l + 1:
        m = (l + r ) // 2
        if count(arr1, arr2, m, k):
            l = m
        else:
            r = m
    return l,r



n,k = [int(x) for x in input().split()]

arr1 = [int(x) for x in input().split()]
arr2 = [int(x) for x in input().split()]

arr1.sort()
arr2.sort()

l,r = binary_search(arr1, arr2, k-1)
print(r)


def test():
    import random
    N = random.randint(0,100)
    arr1 = [random.randint(0,100) for _ in range(N)]
    arr2 = [random.randint(0,100) for _ in range(N)]
    # arr1 = [40, 40, 50, 75]
    # arr2 = [13, 29, 50, 57]

    # arr1, arr2, N = [4,2,6,4,8], [7,3,1,9,5], 5
    arr1, arr2, N = [1,2,3,4], [1,2,3,4], 4
    arr1.sort()
    arr2.sort()
    expected = []
    for x in arr1:
        for y in arr2:
            expected.append(x+y)
    expected.sort()


    for k in range(N*N):
        l,r = binary_search(arr1,arr2,k)
        if r != expected[k]:
            raise Exception(f"not equal at {k} L={l}, r={r}", (l,r), expected[k], arr1, arr2, expected)
        else:
            print(f"working for {k} {r} {expected[k]}, {expected}")

test()

"""
runtime analysis:

binary_search : log(Ans)
count         : N*log(N)
======================
log(Ans)*N*log(N)

"""