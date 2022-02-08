import sys

if sys.version_info[0] < 3:
    from io import BytesIO as stream
else:
    from io import StringIO as stream

sys.stdin = stream(sys.stdin.read())
input = lambda: sys.stdin.readline().rstrip('\r\n')

def bisect_left(arr, x):
    """
    x = 5
          L      R
      1 3 4      10 10
   arr[i] <5 |   5 <= arr[i]


   x = 2
      L              R
      1              3 4 10 10
   arr[0..L] < 2 |   2 <= arr[R..N]
    """
    N = len(arr)
    l = -1  # arr[l] <  x
    r = N   # arr[r] >= x
    while r > l + 1:
        m = (l + r) // 2
        if arr[m] < x:
            l = m
        else:
            r = m
    return l
    
        


def bisect_right(arr, x):
    """
    x = 5
            L    R
        1 3 4    10 10
   arr[i] <= 5 |   5 < arr[i]
    
    """
    N = len(arr)
    l = -1   # arr[l] <= x
    r = N    # arr[r] > x
    while r > l + 1:
        m = (l + r) // 2
        if arr[m] <= x:
            l = m
        else:
            r = m
    return r


n = int(input())
arr = [int(x) for x in input().split()]
q = int(input())

arr.sort()

out = []
for x in range(q):
    lo,hi = [int(x) for x in input().split()]
    L = bisect_left(arr, lo)
    R = bisect_left(arr, hi+1)
    # print(arr, lo,hi,L, R)
    out.append(R - L)
    # print(R - L)

out = map(str, out)
print(" ".join(out))