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


    # print("k = 0", cs)
    # print("k = 0", ps)

    k = 0
    while (1 << k) < N+1:
        xs = []
        for i in range(L):
            pair = (cs[i],cs[(i + (2**k)) % L]), i
            xs.append(pair)
        xs.sort()
        
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
            # print("breaking", k)
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
