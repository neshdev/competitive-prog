n = int(input())
upper_sum , lower_sum = 0, 0
arr = []
for _ in range(n):
    upper, lower = [int(x) for x in input().split()]
    upper_sum += upper
    lower_sum += lower
    arr.append((upper, lower))

if (upper_sum % 2) == 0 and (lower_sum % 2) == 0:
    print("0")
else:
    msg = "-1"
    for upper, lower in arr:
        U = upper_sum - upper
        L = lower_sum - lower
        U += lower
        L += upper
        if U % 2 == 0 and L % 2 == 0:
            msg = "1"
            break
    print(msg)