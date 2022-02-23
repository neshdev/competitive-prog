"""

[a1 a2 a3 a4 .. an] [b1, b2 b3 ... bm]

a1 <= a2 <= ... <= an
b1 >= b2 >= ... >= bm

We need to maximize the window with overlap

for ex:
N=3
M=4
(n,m) -> means that there are n elements of weight X and m elements of weight Y

0,0 1,0 2,0 3,0
0,1 1,1 2,1 3,1
0,2 1,2 2,2 3,2
0,3 1,3 2,3 3,3
0,4 1,4 2,4 3,4

we can get the extremes by the following:
is all elements from M
0,0
0,1
0,2
0,3
0,4

is all elements from N
0,0 1,0 2,0 3,0

At maximum, we can have all N + M elements as part of our costs.

We need a compromise of N and M where the costs are maximized from both regions.

This is exactly the region somewhere between A[L..R]

A = [a1 a2 a3 b1 b2 b3 b4]

for ex, we can pick A[a2..b3], which implies
that b1 b2 b3 are the most expensive costs
a2 a3 are the most expensive costs

the L..R window will be satisfying the constraint <= S
"""

n, m, s, X, Y = [int(x) for x in input().split()]

xs = [(int(x), X) for x in input().split()]
ys = [(int(x), Y) for x in input().split()]


def two_pointer(xs,ys,s):
    arr = sorted(xs) + sorted(ys, reverse=True)
    l = 0

    def good():
        return total_weight <= s

    def add(i):
        global total_weight
        global total_cost
        c, w = arr[i]
        total_weight += w
        total_cost += c

    def remove(i):
        global total_weight
        global total_cost
        c, w = arr[i]
        total_weight -= w
        total_cost -= c

    global total_weight
    global total_cost
    total_weight = 0
    N = len(arr)
    total_cost = 0
    best = float("-inf")
    for r in range(N):
        add(r)
        while not good():
            remove(l)
            l += 1

        best = max(total_cost, best)
    return best


ans = two_pointer(xs,ys,s)
print(ans)


def test():
    import random
    test_cases = 1000
    for _ in range(test_cases):
        N = random.randint(1, 10)
        M = random.randint(1, 10)
        arr1 = [random.randint(1, 10) for i in range(N)]
        arr2 = [random.randint(1, 10) for i in range(M)]

        arr1.sort(reverse=True)
        arr2.sort(reverse=True)

        S = random.randint(1, (sum(arr1) + sum(arr2)) // 2)
        X = random.randint(1, 10)
        Y = random.randint(1, 10)

        dp1 = [0]*(N+1)
        dp2 = [0]*(M+1)

        for i in range(1, N+1):
            dp1[i] = dp1[i-1] + arr1[i-1]
        for i in range(1, M+1):
            dp2[i] = dp2[i-1] + arr2[i-1]

        best = float('-inf')
        for i in range(N+1):
            for j in range(M+1):
                if i*X + j*Y <= S:
                    best = max(best, dp1[i] + dp2[j])
                    # print(i,j,"--",f"{i*X} + {j*Y}", f"weight={i*X + j*Y} <= {S}", f"cost={dp1[i] + dp2[j]}" )

        xs = zip(arr1, [X]*N)
        ys = zip(arr2, [Y]*M)
        actual = two_pointer(xs,ys,S)
        if actual != best:
            raise Exception(
                f"error {actual} != {best}, N,M,arr1,arr2,S,X,Y={N},{M},{arr1},{arr2},{S},{X},{Y}")

        print(S, X, Y)
        print(arr1, dp1)
        print(arr2, dp2)
        print(best, actual)

# test()


"""
Option 1:
combining and sorting by costs

fails for input below:
having both weights next to each other isnt a good thing

7 6 12 5 3
12 10 9 8 7 7 3 
8 7 5 4 3 1

See details for implementation #2 above

"""
