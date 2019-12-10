def dfs(x, y, k, n):
    global cnt
    global tc
    if k == 7:
        if visit[n] != tc:
            cnt += 1
            visit[n] = tc
        return

    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if tx < 0 or tx >= 4 or ty < 0 or ty >=  4: continue
        dfs(tx, ty, k + 1, n * 10 + data[tx][ty])

import sys
sys.stdin = open("input_2819.txt")
T = int(input())
visit = [0] * 10000000
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for tc in range(1, T+1):
    data = [[0 for _ in range(4)] for _ in range(4)]
    cnt = 0
    for i in range(4):
        data[i] = list(map(int, input().split()))

    for i in range(4):
        for j in range(4):
            dfs(i, j, 1, data[i][j])

    print("#{} {}".format(tc, cnt))