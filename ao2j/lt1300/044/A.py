n = int(input())
stats  = {}
for _ in range(n):
    s = input()
    stats[s] = stats.get(s,0) + 1

best_value = float('-inf')
best_key = None
for k,v in stats.items():
    # print(k,v)
    if v > best_value:
        best_value = v
        best_key = k 

print(best_key)