year = int(input())+1

for num in range(year, 10000):
    elements = set()
    arr = []
    while num:
        num,r = divmod(num,10)
        elements.add(r)
        arr.append(r)
    if len(elements) == 4:
        total = 0
        for i in range(4):
            total += arr[i]*10**i
        print(total)
        break