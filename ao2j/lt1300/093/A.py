n = int(input())
raw = [int(x) for x in input().split()]
flipped = [1-x for x in raw]

def make_dp(arr):
    dp = [0]*n

    for i in range(n):
        dp[i] = dp[i-1] + arr[i]
    return dp

def query(arr):
    """
    arr =   0   1   2   3   4
    dp  =   0   1   3   6   10
    0 <= lo <= hi < n
    """
    arr = make_dp(arr)
    def _query(lo, hi):
        # print(lo,hi)
        if hi < lo:
            return 0
        if lo < 0:
            return 0
        elif lo == 0:
            return arr[hi]
        else:
            return arr[hi] - arr[lo-1]
    return _query

def solve():
    """
    time: O(n^2)
    space: O(n)
    """
    qraw = query(raw)
    qinv = query(flipped)
    best = 0
    for i in range(n):
        for j in range(i,n):
            before = qraw(0, i-1)
            window1 = qinv(i,j)
            after = qraw(j+1, n-1)
            # print(i,j, before, after)

            s1 = before + window1 + after

            # if s1 > best:
            #     print(i, j, s1)
            best = max(s1,best)

    print(best)

def solve2():
    """
    time: O(n)
    space: O(n)
    """
    arr = [1 if x == 0 else -1  for x in raw]
    dp = [0]*(n+1)
    for i in range(1, n+1):
        dp[i] = max(dp[i-1] + arr[i-1], arr[i-1])
    S = raw.count(1)
    best = 0
    for i in range(n+1):
        best = max(best, dp[i])
    if best > 0:
        print(best + S)
    else:
        print(S-1)

solve2()