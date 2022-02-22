n, s = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]


def two_pointer(arr, s):
    l = 0

    global dp

    N = len(arr)
    min_segment = float('inf')

    def add(r):
        global dp
        N = r-l+1

        dp = [[False for _ in range(s+1)] for _ in range(N+1)]

        for y in range(N+1):
            dp[y][0] = True

        for y,val in enumerate(arr[l:r+1],start=1):
            # print("at y", y)
            for x in range(1, s+1):
                if x-val >= 0:
                    dp[y][x] = dp[y-1][x] or dp[y-1][x-val]
                else:
                    dp[y][x] = dp[y-1][x] 


    def remove(r,l):
        global dp
        N = r-l+1

        dp = [[False for _ in range(s+1)] for _ in range(N+1)]

        for y in range(N+1):
            dp[y][0] = True

        for y,val in enumerate(arr[l:r+1],start=1):
            for x in range(1, s+1):
                if x-val >= 0:
                    dp[y][x] = dp[y-1][x] or dp[y-1][x-val]
                else:
                    dp[y][x] = dp[y-1][x] 

    def good():
        return dp[-1][-1]

    for r in range(N):
        add(r)
        ok = False
        while good():
            l += 1
            remove(r,l)
            ok = True
 
        if ok:
            min_segment = min(min_segment, r-l+2)
            # print((l-1,r),(r-l+1))
    return min_segment


ans = two_pointer(arr, s)
print(ans)
