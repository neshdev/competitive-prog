n = int(input())
arr = [int(x) for x in input().split()]

ticket_cost = 25
bank = 0
msg = "YES"


bills = {
    25: 0,
    50: 0,
}

for i in range(n):
    if arr[i] == 25:
        bills[25] += 1
    elif arr[i] == 50:
        if bills[25] > 0:
            bills[25] -= 1
        else:
            msg = "NO"
            break
        bills[50] += 1
    else:
        if bills[50] > 0 and bills[25] > 0:
            bills[50] -= 1
            bills[25] -= 1
        elif bills[25] >= 3:
            bills[25] -= 3
        else:
            msg = "NO"
            break
print(msg)