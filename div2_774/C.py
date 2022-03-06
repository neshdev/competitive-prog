def fact_or_poweroftwo(n):
    factorials = [6]
    product = 6
    i = 3
    while product <= min(10**12,n):
        i += 1
        product *= i
        factorials.append(product)

    acc = []
    combo(factorials, 0, [], acc)

    best = float('inf')
    for xs in acc:
        num = n
        for x in xs:
            num -= x
        if num >= 0:
            best = min(best, len(xs) + ones(num))
    return best

def combo(arr, i, curr, acc):
    N = len(arr)
    if i >= N:
        acc.append(curr)
    else:
        copy = list(curr)
        copy.append(arr[i])
        combo(arr, i+1, copy, acc) 
        combo(arr, i+1, curr, acc)

def ones(n):
    return bin(n).count('1')
    

t = int(input())
out = []
for _ in range(t):
    n = int(input())
    ans = fact_or_poweroftwo(n)
    out.append(ans)

out = map(str, out)
print("\n".join(out))