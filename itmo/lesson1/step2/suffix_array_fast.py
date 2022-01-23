
def count_sort(ps, cs):
    """
    L = |ps| = |cs|
    This runs in O(L) time
    """
    L = len(ps)
    buckets = [0]*L
    for val in cs:
        buckets[val] += 1

    pos = [None]*L
    pos[0] = 0
    for i in range(1,L):
        pos[i] = pos[i-1] + buckets[i-1]

    ps_new = [None]*L
    for x in ps:
        i = cs[x]
        ps_new[pos[i]] = x
        pos[i] += 1
    return ps_new

    
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

    # print(cs,ps)

    k = 0
    while (1 << k) < N+1:
        """
        k -> k + 1
        """
        for i in range(L):
            ps[i] = (ps[i] - ( 1 << k) + L) % L

        ps = count_sort(ps, cs)
        # print(ps)
        
        high = 0
        cs_new = [None]*L
        cs_new[ps[0]] = 0
        for i in range(1,L):
            prev = cs[ps[i-1]], cs[(ps[i - 1] + (1 << k)) % L]
            now = cs[ps[i]], cs[(ps[i] + (1 << k)) % L]
            if (now == prev):
                cs_new[ps[i]] = cs_new[ps[i-1]]
            else:
                cs_new[ps[i]] = cs_new[ps[i-1]] + 1
            high = max(high, cs_new[ps[i]])

        cs = cs_new

        if high == L-1:
            break
        k += 1

    # for i in range(L):
    #     k = ps[i]
    #     print("".join(arr[k:]))
    # print(end="")
    for i in range(L):
        print(ps[i], end = " ")
        
s = input()
# s = "ababba"

suffix(s)

