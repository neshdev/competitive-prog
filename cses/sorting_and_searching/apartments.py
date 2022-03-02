n, m, k = [int(x) for x in input().split()]
applicants = [int(x) for x in input().split()]
apartments = [int(x) for x in input().split()]


applicants.sort()
apartments.sort()

total = 0
i = 0
j = 0
while i < n and j < m:
    # print(i,j)
    if applicants[i]-k <= apartments[j] <= applicants[i]+k:
        total += 1
        i += 1
        j += 1
    elif applicants[i] > apartments[j]:
        j += 1
    else:
        i += 1

print(total)


# 4 3 5
# 45 60 60 80
# 30 60 75
