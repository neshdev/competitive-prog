from collections import deque

def reduction(num):
    num = [ord(x) - ord('0') for x in num]
 
    N = len(num)
 
    for i in range(N-2,-1,-1):
        total = num[i] + num[i+1]
        # print(x,y,total)
        q,r = divmod(total,10)
        if q:
            num[i] = 1
            num[i+1] = r
            return to_answer(num)
    
    num[1] += num[0]
    num.pop(0)
    return to_answer(num)


def to_answer(nums):
    return "".join(str(x) for x in nums)

t = int(input())
for _ in range(t):
    num = list(input())
    ans = reduction(num)
    print(ans)

"""


x
98765
17765

 x
98765
91565

  x
98765
98135

   x
98765
98711 **

================================
x
12345
3345   **

 x
12345
1545
   
  x 
12345
1275

  x 
12345
1279
===============================
x
12912
3987

 x
12912
11112

  x
12912
12102 **

   x
12912
1213 
==============================
x
98123
17123  **

 x
98123
9923

  x
98123
9833

   x
98123
9815
=============================

8127
927

8127
837

819
"""
