n, m, s, X, Y = [int(x) for x in input().split()]

xs = [int(x) for x in input().split()]
ys = [int(x) for x in input().split()]


def two_pointer(n, m, s, X, Y, xs, ys):
    xs.sort(reverse=True)
    ys.sort(reverse=True)

    global total_cost
    global x_pos
    global total_weight

    l = 0
    x_pos = -1
    total_weight = 0
    total_cost = 0
    while x_pos < n-1 and total_weight <= s:
        total_cost += xs[x_pos + 1]
        total_weight += X
        x_pos += 1

    if total_weight > s:
        total_weight -= X
        total_cost -= xs[x_pos]
        x_pos -= 1

    best = total_cost
    
    def add(i):
        global total_cost
        global total_weight
        total_cost += ys[i]
        total_weight += Y

    def remove(i):
        global total_cost
        global total_weight
        global x_pos
        total_cost -= xs[x_pos]
        x_pos -= 1
        total_weight -= X

    def invalid():
        return x_pos >= 0 and total_weight > s

    for r in range(m):
        add(r)
        while invalid():
            remove(l)
            l += 1
        if total_weight > s:
            break
        best = max(best, total_cost)

    return best


ans = two_pointer(n, m, s, X, Y, xs, ys)

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

        actual = two_pointer(N, M, S, X, Y, arr1, arr2)
        if actual != best:
            raise Exception(
                f"error {actual} != {best}, N,M,arr1,arr2,S,X,Y={N},{M},{arr1},{arr2},{S},{X},{Y}")

        print(S, X, Y)
        print(arr1, dp1)
        print(arr2, dp2)
        print(best, actual)

# test()
