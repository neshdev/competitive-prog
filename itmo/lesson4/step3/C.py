
def good(arr, m, k):
    N = len(arr)
    count = 1
    last_pos = 0
    # pos = [0]*N
    # pos[0] = 1
    for curr_pos in range(N):
        if arr[curr_pos] - arr[last_pos] >= m:
            count += 1
            last_pos = curr_pos
            # pos[curr_pos] = 1
    # print(m, count, pos)
    return count >= k

def binary_search(arr, k):
    """
                                        L   R
    0   1   2   3   4   5   6   7   8   9   10  11  12
    T   T   T   T   T   T   T   T   T   T   F
    """
    l = -1
    r = (10**9)+1
    # r = 100
    while r > l + 1:
        m = (l + r) // 2
        if good(arr, m, k):
            l = m
        else:
            r = m
    return l

n,k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]


ans = binary_search(arr, k)
print(ans)


# 2 5 7 11 15 20

# max min   | a[i] - a[j] |
#     i != j