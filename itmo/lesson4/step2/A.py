def good(x, w, h, n):
    return (x // w) * (x // h) >= n


def binary_search(w,h,n):
    """
                L   R
    0   0   0   0   1   1   1   1

    """
    l = 0                #f(l) == 0
    r = max(w,h)*n       #f(r) == 1
    while r > l + 1:
        m = (l + r) // 2
        if good(m,w,h,n):
            r = m
        else:
            l = m
    return r


w, h, n = [int(x) for x in input().split()]
ans = binary_search(w,h,n)
print(ans)