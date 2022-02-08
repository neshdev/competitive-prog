import sys

if sys.version_info[0] < 3:
    from io import BytesIO as stream
else:
    from io import StringIO as stream

sys.stdin = stream(sys.stdin.read())
input = lambda: sys.stdin.readline().rstrip('\r\n')

class SegmentTree:
    def __init__(self, n, f=lambda x,y: x+y, default=0, construct=lambda x: x):
        size = 1
        while size < n:
            size *= 2
        self.arr = [default] * (2*size)
        self.size = size
        self.default = default
        self.f = f
        self.construct = construct

    def build(self, xs):
        N = len(xs)
        for i in range(N):
            self.arr[self.size + i - 1] = self.construct(xs[i])

        for i in range(self.size-2,-1,-1):
            # print(i)
            left = self.arr[i*2+1]
            right = self.arr[i*2+2]
            self.arr[i] = self.f(left,right)



    def __setx(self, i, x, curr, lo, hi):
        # print(f"{hi=},{lo=},{curr=},{i=},{x=}")
        if (hi - lo) == 1:
            self.arr[curr] = self.construct(x)
            return
        m = (lo + hi) // 2
       
        if i < m:
            self.__setx(i,x,curr*2+1,lo, m)
        else:
            self.__setx(i,x,curr*2+2,m, hi)
        
        left = self.arr[curr*2+1]
        right = self.arr[curr*2+2]
        self.arr[curr] = self.f(left, right)


    def setx(self, i , x):
        self.__setx(i,x,0,0,self.size)

    def setx_fast(self, i , x):
        size = self.size
        arr = self.arr 
        arr[size+i-1] = self.construct(x)
        # print(arr[size+i-1])
        pos = (size+i-2) // 2
        # print("original", i, size+i-1)
        while pos > 0:
            # print(pos)
            arr[pos] = self.f(arr[pos*2+1], arr[pos*2+2])
            # print(arr[size+i-1])
            pos = (pos-1) // 2
        arr[pos] = self.f(arr[pos*2+1], arr[pos*2+2])

    def update(self, i, x):
        size = self.size
        arr = self.arr 
        y = arr[size+i-1]
        self.setx(i, x+y)

    def update_range(self, lo, hi, x):
        """
        will add +x to A[lo...hi-1]
        will add -x to A[hi]

        What happens for out of bounds?
        Easiest solution is to 2X the size of the array, so you don't have
        to worry about getting out of bounds on the edge cases in powers of 2

        Args:
            lo
            hi
        """
        self.update(lo, x)
        self.update(hi, -x)


    def __query(self, l, r, curr, lox, hix):
        # print(f"{l=},{r=},{curr=},{lox=},{hix=}")
        """
        3 cases:
        1)   
                        lox-------hix l----------r
           l----------r lox-------hix
        2)   l--------------------------r
                    lox-------hix
        3)          lo----------hi   
                            lox-------hix
                    lo----------hi   
                lox-------hix
                    
        """
        if lox >= r or l >= hix:
            return self.default
        elif lox >= l and hix <= r:
            return self.arr[curr]
        else:
            m = (lox + hix) // 2
            left = self.__query(l, r, curr*2+1, lox, m)
            right = self.__query(l, r, curr*2+2, m, hix)
            return self.f(left, right)
        

    def query(self, lo, hi):
        res = self.__query(lo, hi, 0, 0, self.size)
        return res

    def print(self):
        out = []
        k = 0
        for i in range(self.size-1, self.size*2):
            item = (f"val={self.arr[i]},i={k}",)
            out.append(item)
            k += 1
        return out

    def print_tree(self):
        # print(self.arr)
        out = []
        from collections import deque
        q = deque([(0,0)])
        N = self.size
        while q:
            v,l = q.popleft()
            
            if v < 2*N:
                if len(out) < l+1:
                    out.append([])

                val = self.arr[v]
                out[l].append(val)

                
                q.append((v*2+1,l+1))
                q.append((v*2+2,l+1))
        out.pop()
        return out


MAX_ELEMENTS = 41

default = 0, [False for i in range(MAX_ELEMENTS)]

def merge(a,b):
    ca, freqa = a
    cb, freqb = b
    freq = [False for i in range(MAX_ELEMENTS)]
    count = 0
    for i in range(MAX_ELEMENTS):
        if freqa[i] | freqb[i]:
            freq[i] = True
            count += 1
    return count, freq

def construct(x):
    freq = [False for i in range(MAX_ELEMENTS)]
    freq[x] = True
    return 1,freq


N, M = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
st = SegmentTree(N, merge, default, construct)
st.build(arr)

ans = []
for _ in range(M):
    query = [int(x) for x in input().split()]
    # print(query)
    if query[0] == 1:
        _, _lo, _hi = query     
        val, _ = st.query(_lo-1,_hi)
        ans.append(val)
    else:
        _, x, y = query
        st.setx_fast(x-1,y)
        
ans = map(str, ans)
print("\n".join(ans))


# # # for x in st.print_tree():
# # #     print(x)


# import random
# N = 10
# MAX_UPPER = 40
# arr = [random.randint(0,MAX_UPPER) for i in range(N)]

# def inversions(arr, l, r):
#     inv = 0
#     for end in range(l, r):
#         for i in range(l, end):
#             if arr[i] > arr[end]:
#                 inv += 1
#     return inv
    
# st = SegmentTree(N, merge, default, construct)
# st.build(arr)

# # arr = [7,1,6,1,7,2,2]
# # lo = 0
# # hi = 7
# # expected = inversions(arr, lo, hi)
# # actual, _ = st.query(lo, hi)
# # print(actual, expected, lo, hi)
# # if actual != expected:
# #     raise Exception(actual, expected, arr, lo, hi)

# print(arr)
# M = 100
# for i in range(M):
#     pos = random.randint(0,N-1)
#     val = random.randint(1,MAX_UPPER)
#     arr[pos] = val
#     st.setx_fast(pos, val)
#     print("random update", pos, val, arr)
#     for lo in range(N+1):
#         for hi in range(lo, N+1):
#             expected = inversions(arr, lo, hi)
#             actual, _ = st.query(lo, hi)
#             print(actual, expected, lo, hi)
#             if actual != expected:
#                 raise Exception(actual, expected, arr, lo, hi)
