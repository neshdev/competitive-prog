def find_constraints(arr):
    arr.sort()

    N = len(arr)
    dp = [0]*N
    for i in range(N):
        dp[i] = dp[i-1] + arr[i]
    def sum_at(i,j):
        if i == 0:
            return dp[j]
        else:
            return dp[j] - dp[i-1] 

    for i in range(0,N):
        max_start = N-i-1
        max_end = N-1
        min_start = 0
        min_end = i+1
        # print(arr[max_start: max_end+1], arr[min_start:min_end+1] )
        if min_end < max_start:
            # print(sum_at(max_start, max_end), )
            if sum_at(max_start, max_end) > sum_at(min_start, min_end):
                return "YES"
    return "NO"

t = int(input())
out = []
for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    # print("start",arr)
    ans = find_constraints(arr)
    out.append(ans)

out = map(str, out)
print("\n".join(out))