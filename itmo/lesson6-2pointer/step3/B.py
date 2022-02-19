"""
Given an array of n integers ai. 
Let's say that the segment of this 

array a[l..r] (1≤l≤r≤n) is good if the sum of elements 
on this segment is at most s. 

Your task is to find sum of lengths of all good segments.


sum(r-l) such that a[l..r] <= s


S = 20
7 20
2 6 4 3 6 8 9
            

2
6   2,6
4   6,4     2,6,4
3   4,3     6,4,3   2,6,4,3
6   3,6     4,3,6   6,4,3,6     2,6,4,3,6*
8   6,8     3,6,8   4,3,6,8*    6,4,3,6,8*   2,6,4,3,6,8*
9   8,9     6,8,9*  3,6,8,9*    4,3,6,8,9*   6,4,3,6,8,9*     2,6,4,3,6,8,9*
============================================================================
7   6       5       4           3           2               1

7*1 +
6*2 +
4*3 +
2*4
= 7+12+12+8 = 39


2 properties
1. good(arr, L, R) -> should be fast (1)
2. given a[L..R] <= s and a[i] >= 0

            L                       R
            -------------------------
                l             r
                ---------------

        a[L..R] <= s then a[l..r] <= s
        where L <= l <= r <= R

        R
  L
2 6 4 3 6 8 9


"""


n,s = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]


def compute_lengths(x):
    return x*(x+1) // 2

def two_pointer(arr, s):
    total = 0
    lengths = 0
    l = 0
    N = len(arr)
    for r in range(N):
        total += arr[r]
        while total > s:
            total -= arr[l]
            l += 1
        lengths += compute_lengths(r-l+1)
    return lengths

ans = two_pointer(arr, s)
print(ans)


def test():
    import random
    test_cases = 1000
    for _ in range(test_cases):
        N = random.randint(1,100)
        arr = [random.randint(1,10) for i in range(N)]
        s = random.randint(0,sum(arr))



        total = 0
        N = len(arr)
        for i in range(N):
            for j in range(i,N):
                if sum(arr[i:j+1]) <= s:
                    total += j-i+1
                    # print(arr[i:j+1])

        actual = two_pointer(arr, s)
        if actual != total:
            raise Exception(f"{actual}!={total}")
        else:
            print(actual, arr)
# test()