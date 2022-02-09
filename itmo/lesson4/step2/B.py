import math

def rope_cut_good(arr, c , k):
    total = 0
    for l in arr:
        total += math.floor(l / c)
    return total >= k


def binary_search(arr, k):
    """
                    L   R
    1   1   1   1   1   0   0   0   0   0
    """
    l = 0    # f(l) = 1
    r = 10**7  # f(r) = 0
    for _ in range(100):
        m = (l + r) / 2
        if rope_cut_good(arr,m,k):
            l = m
        else:
            r = m
    return l

n,k = [int(x) for x in input().split()]
arr = []
for _ in range(n):
    l = int(input())
    arr.append(l)

ans = binary_search(arr, k)
print(ans)