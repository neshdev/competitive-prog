"""

        1   3   5
        
        1   3
        3   5

 | arr[L..R] > s |

        L             R
        ---------------
           l      r
           --------


"""

n, r = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

def two_pointer(arr,k):
    l = 0
    N = len(arr)
    count = 0
    for r in range(N):
        while arr[r] - arr[l] > k:
            l += 1
        count += l
    return count

ans = two_pointer(arr, r)
print(ans)