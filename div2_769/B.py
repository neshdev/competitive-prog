from functools import cmp_to_key

def solution(p):
    k = 1
    while 2**k <= p:
        k += 1

    k -=1
    num = 2**k -1
    while num:
        print(num, end=" ")
        num -= 1

    print(num, end=" ")

    for num in range(2**k, p+1):
        print(num, end=" ")

    print("")
        

t = int(input())
for _ in range(t):
    p = int(input())
    solution(p-1)