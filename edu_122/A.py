def least(ans, x):
    if x < ans:
        ans, x = x, ans
    diff = 0
    while x:
        ans, r1 = divmod(ans, 10)
        x, r2 = divmod(x, 10)
        if r1 != r2:
            diff += 1

    while ans:
        ans, r1 = divmod(ans, 10)
        diff += 1

    return diff

N = int(input())
for i in range(N):
    x = int(input())
    if x % 7 == 0:
        print(x)
    else:
        ans1 = (x // 7)+1
        ans1 *= 7

        ans2 = (x // 7)
        ans2 *= 7

        if least(ans1,x) > least(ans2,x):
            print(ans2)
        else:
            print(ans1)
        

