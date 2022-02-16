def good(arr, m, k):
    pairs = []
    for (a,b) in arr:
        item = a - b*m
        pairs.append(item)
    pairs.sort(reverse=True)
    # print("sorted", m, pairs[0:k])
    return sum(pairs[0:k]) <= 0


def binary_search(arr, k):
    """
    """
    l = -1
    r = 10**18
    for _ in range(100):
        m = (l + r) / 2
        if good(arr, m , k):
            r = m
        else:
            l = m
    return r


N,k = [int(x) for x in input().split()]

arr = []
for _ in range(N):
    item = [int(x) for x in input().split()]
    arr.append(item)

X = binary_search(arr, k)
print(X)