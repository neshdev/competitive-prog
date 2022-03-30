x1, y1 = [int(x) for x in input().split()]

if x1 > 0 and y1 > 0:
    p1 = (0,x1+y1)
    p2 = (x1+y1,0)
elif x1 < 0 and y1 > 0:
    x1 = abs(x1)
    y1 = abs(y1)
    p1 = (-(x1+y1), 0)
    p2 = (0, x1+y1)
elif x1 < 0 and y1 < 0:
    x1 = abs(x1)
    y1 = abs(y1)
    p1 = (-(x1+y1), 0)
    p2 = (0, -(x1+y1))
else:
    x1 = abs(x1)
    y1 = abs(y1)
    p1 = (0, -(x1+y1))
    p2 = (x1+y1, 0)

xs = [p1, p2]
xs.sort(key=lambda x: (x[0],x[1]))
out = []
for x,y in xs:
    out.append(x)
    out.append(y)
out = map(str, out)
print(" ".join(out))