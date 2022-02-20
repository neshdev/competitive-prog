n, s = [int(x) for x in input().split()]
ws = [int(x) for x in input().split()]
cs = [int(x) for x in input().split()]


def two_pointer(weights, costs, s):
    N = len(weights)
    l = 0
    best = float('-inf')
    global segment_weight
    global segment_cost
    segment_weight = 0
    segment_cost = 0

    def add(i):
        global segment_weight
        global segment_cost
        segment_weight += weights[i]
        segment_cost += costs[i]

    def remove(i):
        global segment_weight
        global segment_cost
        segment_weight -= weights[i]
        segment_cost -= costs[i]

    def good():
        return segment_weight <= s

    for r in range(N):
        add(r)
        while not good():
            remove(l)
            l += 1

        if segment_cost > best:
            best = segment_cost
    return best


ans = two_pointer(ws, cs, s)
print(ans)
