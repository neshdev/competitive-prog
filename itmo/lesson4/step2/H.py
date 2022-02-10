
def can_make(counter, ns, ps, money):
    def _can_make(x):
        # print("amount of burgers", x)
        total = 0
        for i,count in enumerate(counter):
            available_in_kitchen = ns[i]
            pieces_to_make = count*x
            pieces = max(pieces_to_make - available_in_kitchen, 0)
            total += ps[i]*pieces
        # print("total", total, money)
        return total <= money
    return _can_make


"""
Ex1:

BBBSSC
111223 = 1+1+1+2+2+3 = 10

   b s c
ns 6 4 1
ps 1 2 3
money = 4


3 2 1 -> 1 burger 
buy $3 c
3 2 1 -> 1 burger

===================
2 burgers
"""



"""
Ex2:


BBC
111 = $3

   b s  c
ns 0 10 0
ps 1 10 1
money = $23

can I make 4 burgers?

total = 4*3 = 12$

cost = 4*2 = $8
cost = 4*1 = $4
================
           = $12

$12 <= $23
"""


def binary_search(fn):
    """"
        L   R
    0   1   2   3   4   5
    T   T   F   F   F   F
    
    """
    l = 0           # f(l) = T
    r = 10**13      # f(r) = F
    while r > l + 1:
        m = (r + l) // 2
        if fn(m):
            l = m
        else:
            r = m
    return l


seq = input()
ns = [int(x) for x in input().split()]
ps = [int(x) for x in input().split()]
money = int(input())

def burger_counter(seq):
    counter = [0,0,0]
    for c in seq:
        if c == 'B':
            counter[0] += 1
        if c == 'S':
            counter[1] += 1
        if c == 'C':
            counter[2] += 1
    return counter

counter = burger_counter(seq)

fn = can_make(counter, ns, ps, money)
ans = binary_search(fn)
print(ans)