"""
sum A[l..r] <= s

count [l,r] pairs


7 20
2 6 4 3 6 8 9

2+6+4+3 6+4+3+6

"""


def two_pointers(arr, s):
    N = len(arr)
    l = 0
    total = 0
    count = 0
    for r in range(N):
        total += arr[r]
        while total > s:
            total -= arr[l]
            l += 1
        count += (r - l + 1)
        # print(l,r)
    return count


n, k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]


ans = two_pointers(arr, k)
print(ans)


# def test():
#     import random
#     test_cases = 100
#     for i in range(test_cases):
#         print(i)
#         N = random.randint(1, 100)
#         arr = [random.randint(1,10) for _ in range(N)]
#         s = random.randint(1, 10)

#         # arr, s = [3, 4, 1, 1, 8], 3

#         count = 0
#         for i in range(N):
#             for j in range(i, N):
#                 # print(i,j)
#                 if sum(arr[i:j+1]) <= s:
#                     count += 1

#         actual = two_pointers(arr, s)

#         if actual != count:
#             raise Exception(f"invalid {arr=} {s=} {actual=} != {count=}")
#         else:
#             print(f"working {arr=} {s=} {actual=} != {count=}")

# test()
