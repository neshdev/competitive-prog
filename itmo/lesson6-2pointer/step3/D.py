N = int(input())
caps = [int(x) for x in input().split()]

M = int(input())
shirts = [int(x) for x in input().split()]

O = int(input())
pants = [int(x) for x in input().split()]

P = int(input())
shoes = [int(x) for x in input().split()]

CAPS = 0
SHIRTS = 1
PANTS = 2
SHOES = 3


def two_pointer(caps1, shirts1, pants1, shoes1):
    diff = float('inf')
    

    xs = (list(zip(caps1, [CAPS]*N)) +
          list(zip(shirts1, [SHIRTS]*M)) +
          list(zip(pants1, [PANTS]*O)) +
          list(zip(shoes1, [SHOES]*P)))

    xs.sort(key=lambda x: x[0])

    counter = [0]*4
    global nums
    nums = 0
    ans = [None]*4
    l = 0

    def smallest():
        # print(current)
        return nums < 4

    def add(i):
        global nums
        _, enum = xs[i]
        counter[enum] += 1
        if counter[enum] == 1:
            nums += 1

    def remove(i):
        global nums
        _, enum = xs[i]
        counter[enum] -= 1
        if counter[enum] == 0:
            nums -= 1

    T = len(xs)
    L = 0
    R = len(xs)-1

    # print(xs)
    for r in range(T):
        add(r)
        ok = False
        while not smallest():
            remove(l)
            l += 1
            ok = True
        # print((l,r), diff, nums)
        if ok:
            if diff > xs[r][0] - xs[l-1][0]:
                diff = xs[r][0] - xs[l-1][0]
                L = l-1
                R = r

    for idx, type in xs[L:R+1]:
        ans[type] = idx

    for x in range(4):
        print(ans[x], end=' ')
    print(end="\n")
    # print(diff, L,R)


two_pointer(caps, shirts, pants, shoes)
