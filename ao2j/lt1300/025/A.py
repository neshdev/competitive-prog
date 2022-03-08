from re import A


n,k,l,c,d,p,nl,np = [int(x) for x in input().split()]

A = k*l // (n * nl)
B = c*d // n
C = p // (n * np)

print(min(A,B,C))