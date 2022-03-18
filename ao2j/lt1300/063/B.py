from collections import Counter

s  = input()

freq = Counter(s)
rem = []
for k,v in freq.items():
    if v % 2 == 1:
        rem.append(k)
if len(rem) == 0:
    print("First")
else:
    if len(rem) % 2 == 0:
        print("Second")
    else:
        print("First")

