n = int(input())

left = []
right = []
for i in range(n):
    a, b = [int(x) for x in input().split()]
    left.append(a)
    right.append(b)


count = 0
for i in range(n):
    found = False
    for j in range(n):
        
        if left[i] == right[j] and i != j:
            # print(left[i], i,j)
            found = True
            break
    if found:
        count += 1


print(n-count)