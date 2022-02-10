from math import sqrt


def good(x, c):
    return x*x + sqrt(x) <= c

def binary_search(c):
    """
          L R
    1 2 3 4 5 6 7 8 9
    T T T T F F F F F
    """
    l = 0
    r = c
    for i in range(100):
        m = (l + r) / 2
        if good(m, c):
            l  = m
        else:
            r = m
    return l

c = float(input())
ans = binary_search(c)
print(ans)