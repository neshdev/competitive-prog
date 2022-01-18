def ap(arr):
    a,b,c = arr
    d1 = b-a
    ansA: float = (b + d1) / c
    ansA = ansA.is_integer() and ansA > 0


    d2 = c-b
    ansB: float = (b - d2) / a
    ansB = ansB.is_integer() and ansB > 0

    d3 = (c - a) / 2
    ansC: float = (a + d3) / b
    ansC = ansC.is_integer() and ansC > 0

    # print(ansA, ansB, ansC)

    return "YES" if any([ansA, ansB, ansC]) else "NO"

t = int(input())
for _ in range(t):
    arr = [int(x) for x in input().split()]
    ans = ap(arr)
    print(ans)