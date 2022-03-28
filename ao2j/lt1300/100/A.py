a,b,n = [int(x) for x in input().split()]

num = a*10
found = False
for x in range(10):
    if (num + x) % b == 0:
        num += x
        found = True
        break
if found:
    print(num, end='')
    rem = ['0']*(n-1)
    print("".join(rem))
else:
    print("-1")
    