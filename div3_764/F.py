import sys
"""
https://codeforces.com/contest/1624/problem/F

Quotient changing lets us eliminate a section. This elimination will be lg(n)
"""


n = int(input())

def query(c):
    print(f"+ {n - c}")
    sys.stdout.flush()
    rem = int(input())
    return rem

def answer(x):
    print(f"! {x}")
    sys.stdout.flush()


lo = 1
hi = n 
rem = 0
while hi - lo > 1:
    m = (lo + hi) // 2
    remn = query(m)
    if remn == rem:
        """
        found in 
        (l,m]
        """
        hi = m
    else:
        """
        found in
        [m,r)
        """
        lo = m
    lo = (lo + n - m) % n
    hi = (hi + n - m) % n
    if(hi == 0): hi = n
    rem = remn  
    
answer(rem*n + lo)

"""
x = 2
n = 24

x = 2 + 12 = 14 
14 % 24 = 0
x = 14 + 6 = 20
20 % 24 = 0
x = 20 + 3 = 23
23 % 24 = 0
x = 23 + 1 = 24
"""
