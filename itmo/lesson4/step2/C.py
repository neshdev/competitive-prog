def good(seconds,needed_number_of_copies,x_seconds,y_seconds):
    """
    This function is a little tricky

    We need to make 2 copies as fast as possible. To do this, we need to use the copier that uses the minimum amount of time. 
    This minimum copier needs to run once to generate an extra copy

    Consequently, copier 2 can start only after a copy has been created. Therefore, it wil have less time to complete the work. 

    For example:
    Given N=7, X=4 and Y=9

    Lets see if can accomplish 7 pieces of work in 25 seconds

    For the fast copier, we can just let it run until time runs out
        floor(25 seconds / 4 seconds) = 6 copies
    For the second copier, we can only start when we have a second copy.
    Therefore, the second copier can only run for (25 - 4 seconds) = 21 seconds.
    It took us 4 seconds to make the second copy using the first copier.

    For the remaining time, we can let it run until time runs out
        floor(21 seconds / 9 seconds) = 2 copies

    So in total, we can make 6 + 2 = 8 copies

    Therefore, in 25 seconds, we can make at least 7 copies.

    Below is a time diagram

            Original
    0         |
    1         |
    2         |
    3         v
    4         copy(1)                Original
    5         |                      |
    6         |                      |
    7         v                      |
    8         copy(2)                |
    9         |                      |
    10        |                      |
    11        v                      |
    12        copy(3)                v
    13        |                      copy(4)
    14        |                      |
    15        v                      |
    16        copy(5)                |
    17        |                      |
    18        |                      |
    19        v                      |
    20        copy(6)                |
    21        |                      v
    22        |                      copy(7)
    23        v                      
    24        copy(8)
    25        |
    """
    a = seconds // x_seconds
    b = (seconds - x_seconds) // y_seconds
    out = a+b >= needed_number_of_copies
    return out

def binary_search(number_of_copies,x_seconds,y_seconds):
    """
                    L   R
    0   0   0   0   0   1   1   1   1   1

    good(0) = can't make it
    good(1) = can make it
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