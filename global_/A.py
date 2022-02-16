def solution(A,B):
    N = len(A)
    for i in range(N-2,-1,-1):
        aa = sum((x+A[i])**2 for x in A[i+1:])
        bb = sum((x+B[i])**2 for x in B[i+1:])

        ba = sum((x+B[i])**2 for x in A[i+1:])
        ab = sum((x+A[i])**2 for x in B[i+1:])

        if aa + bb >= ba + ab:
            swap(A,B,i)
    
    print(A)
    print(B)
    return cost(A) + cost(B)

def cost(A):
    N = len(A)
    total = 0
    for i in range(N):
        for j in range(i+1,N):
            total += (A[i]+A[j])**2
    return total

def swap(A,B,i):
    A[i], B[i] = B[i], A[i]

t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    ans = solution(A,B)
    print(ans)