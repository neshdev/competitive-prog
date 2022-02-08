N, M = [int(x) for x in input().split()]

# st = SegmentTree(N, merge, default, construct)


ans = []
for _ in range(M):
    query = [int(x) for x in input().split()]
    # print(query)
    if query[0] == 1:
        _, i, height = query     
    else:
        _, l, r, power = query 
        
ans = map(str, ans)
print("\n".join(ans))