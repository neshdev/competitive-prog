n = int(input())

times = []
for _ in range(n):
    h, m = [int(x) for x in input().split()]
    times.append(h*60 + m)

times.sort()

last = times[0]
count = 1
best = 1
for i in range(1, n):
    if times[i] == last:
        count += 1
    else:
        last = times[i]
        count = 1
    best = max(best, count)

print(best)