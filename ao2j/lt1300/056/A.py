s,n = [int(x) for x in input().split()]
arr = []
for _ in range(n):
    x,y = [int(x) for x in input().split()]
    arr.append((x,y))

arr.sort(key=lambda x: x[0])

msg = "YES"
for i in range(n):
    x,y = arr[i]
    if s > x:
        s += y
    else:
        msg = "NO"
        break

print(msg)
