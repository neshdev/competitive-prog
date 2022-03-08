s = set(list(input()))
printer = False
for x in ['H', 'Q', '9' ]:
    if x in s:
        printer = True
        break

if printer:
    print("YES")
else:
    print("NO")