n = int(input())
X,Y,Z = 0,0,0
for _ in range(n):
    x,y,z = [int(x) for x in input().split()]
    X += x
    Y += y
    Z += z
# print(X,Y,Z)
if X or Y or Z:
    print("NO")
else:
    print("YES")