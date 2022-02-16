"""
| unique a[L..R] | <= k

              L                    R
              ----------------------
                    l       r
                    --------

if [L..R] is valid, then [l..r] is also valid

If | unique a[L..R] | <= k, 
then removing any element from L..l or r..R will either
    1.) keep   | unique a[l..r] | == k
    2.) reduce | unique a[l..r] | < k

"""
import sys

if sys.version_info[0] < 3:
    from io import BytesIO as stream
else:
    from io import StringIO as stream

sys.stdin = stream(sys.stdin.read())
input = lambda: sys.stdin.readline().rstrip('\r\n')

n, k = [int(z) for z in input().split()]
arr = [int(z) for z in input().split()]


def two_pointers(arr, k):
    l = 0
    total = 0
    nums = 0
    counts = [0 for i in range(10**6)]
    N = len(arr)

    for r in range(N):
        counts[arr[r]] += 1
        if counts[arr[r]] == 1:
            nums += 1
        while not (nums <= k):
            counts[arr[l]] -= 1
            if counts[arr[l]] == 0:
                nums -= 1
            l += 1
        total += r-l+1
    return total


ans = two_pointers(arr, k)
print(ans)

# def test():
#     import random
#     test_cases = 100
#     for _ in range(test_cases):
#         N = 100
#         arr = [random.randint(0,20) for x in range(N)]
#         K = random.randint(0,10)
#         # arr, K = [19, 18, 18, 4, 20, 19, 13, 0, 14, 0], 4
#         # arr, K = [13, 14, 2, 19, 8], 2

#         expected = 0
#         for i in range(N):
#             for j in range(i, N):
#                 # print(i,j)
#                 freq = set(arr[i:j+1])
#                 if len(freq) <= K:
#                     # print(freq, arr[i:j+1], (i,j))
#                     expected += 1
        
#         actual = two_pointers(arr, K)

#         if actual != expected:
#             raise Exception(f"{actual} != {expected}, {arr}, {K}")
#         else:
#             print(f"working for {actual} {arr}, {K=}")
