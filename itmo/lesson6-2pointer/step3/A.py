n, p = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

# print(arr)
"""

min R-L such that sum a[L..R] >= p

give a[i] >= 0

p = 10
              L R
arr 1 2 3 4 5 4 3 2 1
idx 1 2 3 4 5 6 7 8 9

expected:   3 - starting index 
            3 - length from starting index


time: O(N)
space: O(1)

2 pointer method
* need two properties
1. 
        
        sum a[L..R] >= p

        sum a[L..R,R+1] >= p

        [5 4 3 2 1] >= 10
        [5 4 3 2 1] ++ [1] >= 10
 
2. good(arr, L, R) -> need to run "Fast". In our case this was O(1)

"""


"""
        -----------------
        1           2           3
3   1   4   3   1   4   3   1   4 = 16

"""

def two_pointer(arr, p):
    # print(arr)
    q , rem = divmod(p, sum(arr))
    # print(f"{q, rem}", sum(arr))
    if rem == 0:
        return 0, len(arr)*q
    p = rem
    M = len(arr)
    arr = arr*2
    # print(arr, p)

    l = 0
    N = len(arr)
    total = 0

    start_idx = -1
    min_length = float('inf')
    for r in range(N):
        total += arr[r]
        while total >= p:
            total -= arr[l]
            l += 1
        if l > 0:
            if min_length > r-l+2:
                min_length = min(min_length, r-l+2)
                start_idx = l
    # print(l,r,min_length, arr)
    return (start_idx-1, min_length + M*q)

pos, length = two_pointer(arr, p)
print(pos % n + 1, length)



def test():
    import random
    test_cases = 1000
    for _ in range(test_cases):
        N = random.randint(1,20)
        arr = [random.randint(1,10) for _ in range(N)]
        L = random.randint(1,10)
        p = random.randint(1,sum(arr)*L)

        # arr, p = [8, 2, 1], 22
        # N = len(arr)
        # L = 2

        # arr, p = [3, 9, 10, 1, 6, 4, 6, 1, 5, 10, 4, 7, 2, 10], 57
        # N = len(arr)
        # L = 2

        # arr, p =  [9, 10, 8, 10, 3, 7, 8, 9, 4, 7, 3, 3, 1, 5, 4, 1, 3, 5, 6], 295
        # N = len(arr)
        # L = 10

        # arr, p, L = [5, 3, 10, 1, 3, 7, 4, 6, 8], 73, 3
        # N = len(arr)

        # arr, p, L =  [3, 1, 4], 15, 2
        # N = len(arr)

        # arr, p, L =  [1], 2, 2, 
        # N = len(arr)

        arr2 = [arr[i% N] for i in range((L*2+1)*N)]

        # print("starting for ", arr, p)
        
        expected = float('inf')
        for i in range(len(arr2)):
            for j in range(i,len(arr2)):
                if sum(arr2[i:j+1]) >= p:
                    if expected > j - i + 1:
                        expected = min(expected, j - i + 1)
                        # print("best0", expected, i % N)
                        # print("best", len(arr2), i,j, arr2)

        # L = (p // sum(arr) + 1)
        # actual_start, actual = two_pointer(arr*(L*2+1), p)
        actual_start, actual = two_pointer(arr, p)
        # print(actual_start, actual)

        if actual != expected:
            raise Exception(f" {actual} != {expected},  {arr}, {p}, {L}")
        else:
            print(f" {actual} == {expected},  {arr}, {p}, {L}")


# test()