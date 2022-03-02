s = input()

N = len(s)

best = 1
total = 1
for i in range(1,N):
    if s[i] == s[i-1]:
        total += 1
        best = max(best, total)
    else:
        total = 1

print(best)