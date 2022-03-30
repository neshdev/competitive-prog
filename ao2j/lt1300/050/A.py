k = int(input())
s = input()
freq = {}
for i,c in enumerate(s):
    freq[c] = freq.get(c,0) + 1

count = freq[c]
out = []
broken = False
for c,v in freq.items():
    if v != count or v % k != 0:
        broken = True
        break

if broken if len:
    print(-1)
else:
    q = len(s) // k
    ans = "".join(freq.keys())
    print(q*ans)
    