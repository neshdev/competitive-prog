n = int(input())
arr = [int(x) for x in input().split()]
counter = [0]*1001

for i in range(n):
    counter[arr[i]] += 1

counts = []
for i in range(1001):
    if counter[i] > 0:
        counts.append((counter[i],i))

counts.sort(key=lambda x: (-x[0], x[1]))

q = []
for freq,i in counts:
    q.extend([i]*freq)

j = 0
out = [None]*n
for i in range(0,n,2):
    out[i] = q[j]
    j += 1

for i in range(1,n,2):
    out[i] = q[j]
    j += 1

# print(out)

msg = "YES"
for i in range(1,n):
    if out[i] == out[i-1]:
        msg = "NO"
        break

print(msg)
        