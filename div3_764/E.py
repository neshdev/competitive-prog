def phone_segments(N,M,nums,phone):
    # print("new")
    L = len(phone)+1
    dp = [None]*(L)
    dp[0] = -1

    subsegments = {}

    for i in range(N):
        k = nums[i]
        for start in range(M):
            for end in [2,3]:
                
                segment = k[start:start+end]
                if len(segment) > 1 and start+end <= M:
                    subsegments[segment] = (start+1,start+end+1,i+1, segment)

    for start in range(L):
        for end in [2,3]:
            if start + end <= M:
                segment = phone[start:start+end]
                
                if dp[start] != None and segment in subsegments:
                    dp[start+end] = subsegments[segment]
    
    if dp[-1] == None:
        print("-1")
    else:
        k = M
        arr = []
        while k > 0:
            s,e,i,x = dp[k]
            arr.append(dp[k])
            k -= (e-s)
        
        print(len(arr))
        for s,e,i,x in reversed(arr):
            print(f"{s} {e-1} {i}")

t = int(input())
for tc in range(t):
    blank = input()
    N,M = [int(x) for x in input().split()]
    nums = []
    for i in range(N):
        num = input()
        nums.append(num)
    new = input()
    # print(N,M,new)
    phone_segments(N,M,nums,new)
print()
    