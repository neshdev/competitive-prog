def dist(sx, sy, ex, ey):
    return (sx-ex)**2 + (sy-ey)**2


n, sx, sy, ex, ey = [int(x) for x in input().split()]
arr = input()

directions = {
    'N': (0, 1),
    'E': (1, 0),
    'W': (-1, 0),
    'S': (0, -1),
}

prev_dist = dist(sx, sy, ex, ey)
if prev_dist != 0:
    count = 0
    msg = "-1"
    for d in arr:
        dx, dy = directions[d]
        nx = sx + dx
        ny = sy + dy
        distance = dist(nx, ny, ex, ey)
        if distance < prev_dist:
            sx = nx
            sy = ny
            prev_dist = distance
        count += 1

        if sx == ex and sy == ey:
            msg = count
            break
    print(msg)
else:
    print("0")
