
n = int(input())
num = input()
arr = [int(c) for c in num]
ls = arr[0:n]
rs = arr[n:]

ls.sort()
rs.sort()

# print(ls)
# print(rs)


strict_less = True
strict_greater = True
for i,j in zip(ls, rs):
    strict_less &= i < j
    strict_greater &= i > j

if strict_less or strict_greater:
    print("YES")
else:
    print("NO")
