def transitions(y,x):
    yield y+1,x
    yield y,x+1
    yield y-1,x
    yield y,x-1

def valid_transitions(arr):
    # print(arr)
    Y = len(arr)
    X = len(arr[0])
    def _f(y0,x0):
        for y,x in transitions(y0,x0):
            if 0 <= y < Y and 0 <= x < X and arr[y][x] != "-":
                yield y,x
    return _f

def opp(player):
    if player == "W":
        return "B"
    else:
        return "W"

def dfs(board, init, visited, tran_fn, ans):
    q = [(init, 'W')]
    while q:
        (y,x), player = q.pop()
        if (y,x) not in visited:
            visited.add((y,x))
            ans[y][x] = player
            for yn,xn in tran_fn(y,x):
                # print((y,x), (yn,xn))
                item = (yn,xn), opp(player)
                q.append(item)


Y,X = [int(x) for x in input().split()] 
board = []
for y in range(Y):
    s = input()
    board.append(s)

def run(board):
    tran_fn = valid_transitions(board)
    Y = len(board)
    X = len(board[0])
    ans = [["-" for _ in range(X)] for _ in range(Y)]
    visited = set()
    for y in range(Y):
        for x in range(X):
            if board[y][x] == '.':
                dfs(board, (y,x), visited, tran_fn, ans)

    ans = ["".join(xs) for xs in ans]
    print("\n".join(ans))

# print(board)
run(board)
# print(list(valid_transitions(board)(0,0)))
