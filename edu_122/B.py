from collections import Counter

def sol(s):
    freq = Counter(list(s))
    print(freq, s)
    a = freq.get('0',0)
    b = freq.get('1',0)
    if a == b:
        return 0
    return min(a,b)

t = int(input())
for i in range(t):
    s = input()
    ans = sol(s)
    print(ans)