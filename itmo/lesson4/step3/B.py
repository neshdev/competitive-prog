# 1 3 2 4 10 8 4 2 5 3

# 1 3 2 | 4 10 | 8 | 4 2 5 3

# 1 3 2 4 | 10 | 8 4 2 | 5 3
# 10 | 10 | 14 | 8


# min max(...)



# 11 - F
# 1 3 2 4 10 8 4 2 5 3
# 1 3 2 | 4 | 10 | 8 | 4 2 | 5 3

# 12 - F
# 1 3 2 4 | 10 | 8 4 | 2 5 3

# 15 - T
# 1 3 2 4 10 8 4 2 5 3
# 1+3+2+4 | 10 | 8 +4+2 | 5+3

# 18 - T
# 1 3 2 4 10 8 4 2 5 3
# 1+3+2+4 | 10+8 | 4+2+5+3
# therefore we can split any segment further
# and still hold the condition
# 1+3+2+4 | 10+8 | 4+2+5+3 ==> 1+3+2+4 | 10+8 | 4+2 | 5+3

# 20 - T
# 1 3 2 4 10 8 4 2 5 3
# 1+3+2+4+10 | 8 4 2 5 | 5+3



# 24 - F
# 1 3 2 4 10 8 4 2 5 3
# 1 3 2 4 10 | 8 4 2 5 3


def good(arr, X, k):

    N = len(arr)
    total = 0
    seg = []
    for i in range(N):
        if arr[i] > X:
            return False
        if total + arr[i] > X:
            seg.append(total)
            total = arr[i]
        else:
            total += arr[i]

    if total > X:
        return False

    seg.append(total)
    # print(X, seg, len(seg) <= k)
    return len(seg) <= k

def max_of_segment(arr, X):
    N = len(arr)
    total = 0
    seg = []
    for i in range(N):
        if total + arr[i] >= X:
            seg.append(total)
            total = arr[i]
        else:
            total += arr[i]
    seg.append(total)
    return max(seg)

def binary_search(arr, k):
    """
            L   R
    0   1   2   3   4   5
    F   F   F   T   T   T
    """
    l = -1
    r = 10**16
    while r > l + 1:
        m = (l + r) // 2
        if good(arr, m, k):
            r = m
        else:
            l = m
    return r

n,k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

X = binary_search(arr, k)

# ans = max_of_segment(arr, X)

print(X)

# for i in range(1,20):
#     good(arr, i, k)