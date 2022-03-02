n = int(input())

ans = [n]
while n != 1:
    if n % 2 == 0:
        n //= 2
    else:
        n *= 3
        n += 1
    ans.append(n)

ans = map(str, ans)
print(" ".join(ans))
