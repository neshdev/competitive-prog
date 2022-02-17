"""
4 6 9 3 6

find min length of a[l..r] where gcd a[l..r] == 1



Ex1:
4 6 8 9 == gcd (4 6 8 9) == 1
then gcd (4 6 8) == 2   (larger to smaller is invalid)

Ex2:
12 16 64 3
gcd (12 16 64)     != 1
then gcd (12 16 )  != 1
then gcd (16 64 )  != 1

if gcd a[L..R] != 1 then gcd a[l..r] != 1
where L <= l <= r <= R
Removing an element will ensure that there will be another gcd and none of the values will be relatively prime

            L                  R
            --------------------
                l      r
                --------    







2,5,9

2 => 1,2
5 => 1,5
9 => 1,3,9


4 6 9 3 6

4 2 1

4 => 1,2,4
6 => 1,2,3,6
9 => 1,3,9
3 => 1,3
6 => 1,3,6


"""
import math
from math import gcd

class Stack:
    def __init__(self):
        self.xs = []
        self.gcds =[0]

    def push(self, x):
        self.xs.append(x)

        # if not self.gcds:
        #     g = x
        # else:
        g = gcd(x, self.gcds[-1])

        self.gcds.append(g)

    def pop(self):
        self.gcds.pop()
        return self.xs.pop()

    @property
    def gcd(self):
        # if len(self):
        return self.gcds[-1]
        # else:
        #     return 1

    def __len__(self):
        return len(self.xs)

    def __str__(self):
        return f"xs={self.xs},gcds={self.gcds}, curr={self.gcd}"


n = int(input())
arr = [int(x) for x in input().split()]


def two_pointer(arr):
    N = len(arr)
    l = 0
    total = float('inf')
    s1 = Stack()
    s2 = Stack()

    def add(x):
        s2.push(x)

    def remove():
        if not s1:
            while s2:
                s1.push(s2.pop())
        s1.pop()

    def good():
        if s1 and s2:
            g = gcd(s1.gcd, s2.gcd)
            return g != 1
        elif s1 and not s2:
            return s1.gcd != 1
        elif s2 and not s1:
            return s2.gcd != 1
        else:
            return True

    for r in range(N):
        add(arr[r])
        # print("add", s1, "|" ,s2)
        while not good():
            remove()
            # print("remove", s1, "|" ,s2)
            l += 1

        if l > 0:
            total = min(total, r - l + 2)

    return -1 if total == float('inf') else total

ans = two_pointer(arr)
print(ans)