n, m = [int(x) for x in input().split()]
arr = [i+1 for i in range(n)]

total = n*(n+1) // 2
# m = m  % total
i = 0
while True:
    # print("val", arr[i])
    if arr[i] <= m:
        m -= arr[i]
    else:   
        break
    i += 1
    i %= n

print(m)