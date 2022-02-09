def good(seconds,needed_number_of_copies,x_seconds,y_seconds):
    a = seconds // x_seconds
    b = (seconds - x_seconds) // y_seconds
    out = a+b >= needed_number_of_copies
    return out

def binary_search(number_of_copies,x_seconds,y_seconds):
    """
                    L   R
    0   0   0   0   0   1   1   1   1   1
    """
    l = 0
    r = (2*10**8)*10
    while r > l + 1:
        m = (l + r) // 2
        # print(f"{l=}",f"{r=}", f"{m=}")
        if good(m, number_of_copies, x_seconds, y_seconds):
            r = m
        else:
            l = m
    return r

n,x,y = [int(x) for x in input().split()]

if x > y:
    x, y = y, x

ans = binary_search(n,x,y)
print(ans)