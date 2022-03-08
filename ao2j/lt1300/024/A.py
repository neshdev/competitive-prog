out = []
for _ in range(2):
    out.extend(input())

messed_up = list(input())

out.sort()
messed_up.sort()

broken = len(out) != len(messed_up)
for i in range(min(len(messed_up),len(out))):
    if out[i] != messed_up[i]:
        broken = True
        break

if broken:
    print("NO")
else:
    print("YES")

