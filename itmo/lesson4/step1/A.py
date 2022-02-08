import sys

if sys.version_info[0] < 3:
    from io import BytesIO as stream
else:
    from io import StringIO as stream

sys.stdin = stream(sys.stdin.read())
input = lambda: sys.stdin.readline().rstrip('\r\n')

def binary_search(arr, x):
    N = len(arr)
    l = -1             # arr[l] < x
    r = N              # arr[r] >= x
    while r > l + 1:
        m = (l+r) // 2
        if arr[m] <= x:
            l = m
        else:
            r = m
    
    if l >= 0 and arr[l] == x:
        return 'YES'
    else:
        return 'NO'


n, k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
queries = [int(x) for x in input().split()]


out = []
for x in queries:
    ans = binary_search(arr, x)
    out.append(ans)
    print(ans)

# print("\n".join(out))