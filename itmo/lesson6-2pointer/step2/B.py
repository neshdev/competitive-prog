"""
N=7 S=20
arr 2 6 4 3 6 8 9
idx 0 1 2 3 4 5 6

find min |r - l + 1| 

where a[l..r] >= S
"""


def solution(arr, s):
    N = len(arr)
    l = 0
    total = 0
    best = float('inf')

    for r in range(N):
        total += arr[r]
        while total - arr[l] >= s:
            total -= arr[l]
            l += 1

        if total >= s:
            best = min(best, r - l + 1)

    return -1 if best == float('inf') else best


n, s = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

ans = solution(arr, s)
print(ans)
