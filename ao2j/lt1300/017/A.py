n = int(input())
lefts = 0
rights = 0
for _ in range(n):
    l,r = [int(x) for x in input().split()]
    lefts += l
    rights += r

def counts(doors, n):
    closed = n - doors
    opened = doors
    if opened > closed:
        return closed
    else:
        return opened


ans = counts(lefts, n) + counts(rights, n)
print(ans)