# import logging

# logging.basicConfig(level=logging.INFO)

# logger = logging.getLogger()


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
    #     logger.info("".join(arr[k:]))
    
    # for i in range(L):
    #     print(ps[i], end = " ")
    # print()
    return ps
        

# s = "ababba"

def find(suffix_arr, original, query):
    # logger.info(f"{suffix_arr}, {original}")
    lo = bin_search(suffix_arr, original, query)
    # logger.info("lo {lo}")

    chars = list(query)
    c = chars.pop()
    x = chr(ord(c) + 1)
    chars.append(x)

    end_query = "".join(chars)
    # logger.info(f"end {end_query}")

    hi = bin_search(suffix_arr, original, end_query)
    # logger.info("hi {hi}")

    return hi - lo

def condition(suffix_arr, original, query, size, pos):
    N = len(query)
    # print(pos+size)
    if pos + size < len(suffix_arr):
        start = suffix_arr[pos+size]
        cs = original[start:start+N]
        # logger.info(f"{cs}, {query}")
        return cs < query
    return False

def bin_search(suffix_arr, original, query):
    pos = 0
    size = (len(suffix_arr) // 2)
    while size >= 1:
        while condition(suffix_arr, original, query, size, pos):
            pos += size
        size //= 2
    return pos
    

def lcp(suffix_arr, original):
    L = len(suffix_arr)
    rank = [None]*L
    for i in range(0,L):
        rank[suffix_arr[i]] = i

    k = 0
    prefix = [0]*(L-1)
    for i in range(0,L-1):

        s1 = suffix_arr[rank[i]]
        s2 = suffix_arr[rank[i] - 1]

        # print(i)
        # print(original[s1:], original[s2:], k)
        
        while s1 + k < L and s2 + k < L and original[(s1 + k)] == original[ (s2 + k)]:
            k += 1

        prefix[rank[i]-1] = k
        k = max(k-1,0)
    return prefix

def unique_substrings(suffix_arr, longest_common_prefix_arr):
    n = sum(longest_common_prefix_arr)
    L = len(suffix_arr) - 1
    return L * (L+1) // 2 - n


def longest_common_substring(suffix_arr, lcp_arr, s1, s2, original):
    L1 = len(s1)

    N = len(suffix_arr)

    eq = [1]*N

    for i in range(N):
        if suffix_arr[i] < L1:
            eq[i] = 2

    lcp_arr[0] = 0

    best = 0
    best_pos = 0
    for i in range(1,N):
        if eq[i] != eq[i-1]:
            if best < lcp_arr[i-1]:
                best = lcp_arr[i-1]
                best_pos = suffix_arr[i]
    return original[best_pos:best_pos+best]

s1 = input() + '#'
s2 = input()
original = s1 + s2 + '$'
suffix_arr = suffix(s1 + s2)
lcp_arr = lcp(suffix_arr, original)
ans = longest_common_substring(suffix_arr, lcp_arr, s1, s2, original)
print(ans)

