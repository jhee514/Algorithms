import sys
sys.stdin = open("input_1018.txt", "r")

def dfs(i, j, cnt=0):
    global min_cnt
    visited = [[0] * m for _ in range(n)]
    stack = [[i, j]]
    visited[i][j] = 1
    while stack:
        cur = stack.pop(-1)
        for dir in range(4):
            y, x = cur[0] + dy[dir], cur[1] + dx[dir]
            if i <= y <= i + 7 and j <= x <= j + 7 and not visited[y][x]:
                if data[y][x] == pan[cur[0]][cur[1]]:
                    cnt += 1
                    if pan[cur[0]][cur[1]] == 'W':
                        pan[y][x] = 'B'
                    else:
                        pan[y][x] = 'W'
                else:
                    pan[y][x] = data[y][x]
                stack.append([y, x])
                visited[y][x] = 1
    if cnt < min_cnt:
        min_cnt = cnt

for _ in range(2):
    n, m = map(int, input().split())
    data = [list(input()) for _ in range(n)]
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    min_cnt = n * m
    for i in range(n - 7):
        for j in range(m - 7):
            pan = [[0] * m for _ in range(n)]
            pan[i][j] = data[i][j]
            dfs(i, j)
            if data[i][j] == 'W':
                pan[i][j] = 'B'
            else:
                pan[i][j] = 'W'
            dfs(i, j, 1)
    print(min_cnt)