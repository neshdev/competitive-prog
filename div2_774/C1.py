"""
redid this problem with bitset, instead of generating combinations.
"""

def fact_or_poweroftwo(n):
    factorials = [6]
    product = 6
    i = 3
    while product <= min(10**12,n):
        i += 1
        product *= i
        factorials.append(product)

    N = len(factorials)
    best = float('inf')
    for mask in range(0,2**N+1):
        num = n
        for i in range(N):
            """
            Both ways are valid and will work
            """
            # if mask & (1 << i):
            if (mask >> i) & 1:
                num -= factorials[i]
        if num >= 0:
            best = min(best,  ones(mask) + ones(num))
    return best 
        
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