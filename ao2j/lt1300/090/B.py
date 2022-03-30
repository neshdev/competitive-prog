n = int(input())
xs = [int(x) for x in input().split()]

ys = sorted(xs)


def query(ys):
    N = len(ys)
    dp = [0]*N
    for i in range(N):
        dp[i] = dp[i-1] + ys[i]

    def _query(lo, hi):
        if lo == 0:
            return dp[hi]
        else:
            return dp[hi] - dp[lo-1]
    return _query

orig = query(xs)
sort = query(ys)

m = int(input())
out = []
for _ in range(m):
    t, lo, hi = [int(x) for x in input().split()]
    if t == 1:
        x = orig(lo-1, hi-1)
    else:
        x = sort(lo-1, hi-1)
    out.append(str(x))

print("\n".join(out))
