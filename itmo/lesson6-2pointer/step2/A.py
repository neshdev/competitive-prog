

"""
N=7 S=20
arr 2 6 4 3 6 8 9
idx 0 1 2 3 4 5 6

find max |r - l + 1| 

where a[l..r] <= S
"""


def solution(arr, s):
    N = len(arr)
    l = 0
    total = 0
    best = 0

    for r in range(N):
        while not total + arr[r] <= s:
            total -= arr[l]
            l += 1
        total += arr[r]
        best = max(r-l+1, best)
        # print(l, r)
    return best


n, s = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

ans = solution(arr, s)
print(ans)
