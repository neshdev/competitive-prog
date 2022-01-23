
def first(xs):
    L = len(xs)
    buckets = [0]*L
    for i in range(L):
        (a,b) ,p = xs[i]
        buckets[b] += 1

    ps = [None]*L
    ps[0] = 0
    for i in range(1,L):
        ps[i] = ps[i-1] + buckets[i-1]

    new = [None]*L
    for (a,b),p in xs:
        new[ps[b]] = (a,b),p
        ps[b] += 1
    return new


def second(xs):
    L = len(xs)
    buckets = [0]*L
    for i in range(L):
        (a,b) ,p = xs[i]
        buckets[a] += 1

    ps = [None]*L
    ps[0] = 0
    for i in range(1,L):
        ps[i] = ps[i-1] + buckets[i-1]

    new = [None]*L
    for (a,b),p in xs:
        new[ps[a]] = (a,b),p
        ps[a] += 1
    return new

def radix_sort(xs):
    xs = first(xs)
    xs = second(xs)
    return xs

    
    """
                0   1   2   3   4   5   6
    buckets     1   3   3

    ps          0   1   4   7   7   7   7
    
    """

def suffix(s):
    N = len(s)
    arr = list(s)
    arr.append("$")
    L = len(arr)

    #position
    ps = [None]*L

    # equivalence class
    cs = [None]*L

    xs = list(zip(arr, range(L)))
    # k == 0
    xs.sort()
    
    for i in range(L):
        ps[i] = xs[i][1]

    cs[ps[0]] = 0
    
    
    for i in range(1,L):
        if xs[i-1][0] == xs[i][0]:
            cs[ps[i]] = cs[ps[i - 1]]
        else:
            cs[ps[i]] = cs[ps[i - 1]] + 1

    print(cs,ps)

    k = 0
    while (1 << k) < N+1:
        # for i in range(L):
        #     ps[i] = (ps[i] - ( 1 << k) + L) % L


        xs = []
        for i in range(L):
            pair = (cs[i],cs[(i + (2**k)) % L]), i
            xs.append(pair)

        xs = radix_sort(xs)
        
        for i in range(L):
            ps[i] = xs[i][1]
        
        cs[ps[0]] = 0
    
        high = cs[0]
        for i in range(1,L):
            if xs[i-1][0] == xs[i][0]:
                cs[ps[i]] = cs[ps[i - 1]]
            else:
                cs[ps[i]] = cs[ps[i - 1]] + 1

            high = max(high, cs[ps[i]])
        if high == L-1:
            break
        k += 1

    for i in range(L):
        k = ps[i]
        print("".join(arr[k:]))
    print(end="")
    for i in range(L):
        print(ps[i], end = " ")
        
s = input()
# s = "ababba"

suffix(s)

