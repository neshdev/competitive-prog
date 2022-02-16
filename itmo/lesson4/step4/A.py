
def prefix(arr):
    N = len(arr)
    dp = [0]*N
    dp[0] = arr[0]
    for i in range(1,N):
        dp[i] = dp[i-1] + arr[i]
    def f(lo, hi):
        if lo == 0:
            return dp[hi]
        else:
            return dp[hi] - dp[lo-1]
    return f

def good(nums, mid, k):
    sum = 0
    prev = 0
    min_sum = 0
    for i in range(k):
        sum += nums[i] - mid
    if (sum >= 0):
        return True
    for i in range(k, len(nums)):
        sum += nums[i] - mid
        prev += nums[i - k] - mid
        min_sum = min(prev, min_sum)
        if (sum >= min_sum):
            return True
    return False

from typing import List

def pos_good(a: List[int], M, d):
    # a.insert(0,0)
    n = len(a)
    pre = [None]*(n+1)
    pmin = [None]*(n+1)
    pminidx = [None]*(n+1)

    pre[0] = a[0] - M
    pmin[0] = pre[0]
    pminidx[0] = 0
    for i in range(1, n+1):
        pre[i] = pre[i-1] + a[i-1] - M

        if (pre[i] < pmin[i-1]):
            pmin[i] = pre[i]
            pminidx[i] = i
        else:
            pmin[i] = pmin[i-1]
            pminidx[i] = pminidx[i-1]
        

    for R in range(d, n+1):
        if (pre[R] >= pmin[R-d]):
            L = pminidx[R-d] + 1
            return (L-1, R-1)

    return (-1, -1)
def binary_search(arr, d):
    """

                L   R
    0   1   2   3   4   5
    T   T   T   T   F   F
    """
    l = -1
    r = 101
    for _ in range(100):
        m = (l + r) / 2
        if good(arr,m,d):
            l = m
        else:
            r = m
    return l

def sol(arr, d):
    m = binary_search(arr,d)
    (L,R) = pos_good(arr,m,d)
    print(f"{L+1} {R+1}")


def test():
    import random
    n = 10 # random.randint(1,10)
    arr = [random.randint(0,100) for i in range(n)]
    d = random.randint(1,n)
    # arr = [22, 95, 87, 84, 92, 56, 42, 1, 57, 10]
    # arr,d = [85, 48, 94, 63, 98, 54, 68, 46, 92, 0], 10
    # arr,d = [28, 65, 59, 69, 5, 14, 14, 11, 93, 61], 5
    # arr, d = [18, 50, 4, 38, 31, 46, 30, 15, 7, 95], 9
    # arr, d = [17, 16, 5, 97, 98, 50, 42, 5, 11, 50], 1
    # arr, d = [75, 17, 6, 8, 69, 45, 55, 32, 93, 81], 2
    # arr, d = [89, 23, 11, 15, 65, 92, 59, 96, 59, 81], 2

    def brute_force_sol(arr, d):
        query = prefix(arr)

        N = len(arr)

        best = float('-inf')
        L = -1
        R = -1
        for r in range(N):
            for l in range(r+1):
                if r-l+1 >= d:
                    x = query(l,r)                    
                    ev = x / (r-l+1)
                    if best < ev:
                        best = ev
                        L = l
                        R = r
        # print("best", best)
        return best, (L,R)


    for _ in range(1000):
        print(arr, d)
        bt_sol, (LA,RA) = brute_force_sol(arr, d)
        print(bt_sol, (LA,RA))
        m = binary_search(arr,d)
        (L,R) = pos_good(arr,m,d)
        print(m, (L,R) )
        if not (LA == L and RA == R):
            raise Exception(arr, d)

if __name__ == "__main__":
    N,d = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    sol(arr,d)
    # test()