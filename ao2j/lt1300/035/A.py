a,b,c = [int(x) for x in input().split()]

L = (a*b/c)**(1/2)
H = b / L
W = c / H

ans = 4*L + 4*H + 4*W
print(int(ans))