n = int(input())
arr = [int(x) for x in input().split()]

X = sum(arr)
X -= 1
r = X % (n+1)
count = 0
# print("sum", X)
for f in range(5):
    r += 1
    r %= (n+1)
    if r == 0:
        count += 1
print(5-count) 