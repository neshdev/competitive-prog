x = int(input())

lucky_count = 0
while x:
    x,r = divmod(x,10)
    if r in (4,7):
        lucky_count += 1

if lucky_count in (4,7):
    print("YES")
else:
    print("NO")