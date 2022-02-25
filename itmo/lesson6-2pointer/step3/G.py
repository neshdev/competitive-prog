"""
this problem was worded very confusingly. I wasn't able to build a test case.

N = |s|
Find the max length of s where
count of all pairs (i,j) such that arr[i]='a' and arr[j]='b' <= k
where i < j
and for all  arr[L..R] such that 0 <= L <= R <= N
"""

n, k = [int(x) for x in input().split()]
s = input()


def two_pts(s,n,k):
    l = 0
    global total
    total = 0
    counter = [0]*26
    def add(i):
        global total
        if s[i] == 'b':
            total += counter[0]

        c = ord(s[i]) - ord('a')
        counter[c] += 1

    def remove(i):
        global total
        if s[i] == 'a':
            total -= counter[1]

        c = ord(s[i]) - ord('a')
        counter[c] -= 1

    def good():
        return total <= k
    
    best = 0
    for r in range(n):
        add(r)
        while not good():
            remove(l)
            l += 1
        best = max(best, r-l+1)
    return best

ans = two_pts(s, n, k)
print(ans)


# def test():
#     import random
#     for _ in range(100):
#         N = random.randint(2, 20)
#         arr = [chr(random.randint(0, 4) + ord('a')) for i in range(N)]
#         K = random.randint(0,n)
#         a_idx = random.randint(0, N-2)
#         b_idx = random.randint(a_idx, N-1)
#         while b_idx == a_idx:
#             b_idx = random.randint(a_idx, N-1)
#         arr[a_idx] = 'a'
#         arr[b_idx] = 'b'

#         # arr, K= ['t', 'u', 'a', 'v', 'e', 'b', 'v', 'v', 't'], 3
#         # arr, K = ['a', 'j', 'n', 'e', 'a', 'm', 'q', 'b', 'o'], 3
#         # arr, K = ['n', 'p', 'p', 'a', 'l', 'r', 'b', 'x', 'g'], 0
#         N = len(arr)
#         print(arr, K)
#         expected = 0
#         for start in range(N):
#             for end in range(start, N):
#                 print(arr[start:end+1])
#                 if arr[end] == 'b':
#                     count = 0
#                     for j in range(start, end):
#                         if arr[j] == 'a':
#                             count += 1
#                     if count <= K:
#                         expected = max(expected, end-start+1) 

#         actual =two_pts(arr, N, K)
#         if actual != expected:
#             raise Exception(f"{actual=} !={expected=}, arr,K = {arr},{K}")
#         # print(best)

# test()
