import sys

sys.stdin = open("input_1012.txt", "r")

T = int(input())
for _ in range(T):
    n, m, k = map(int, input().split())
    data = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        data[x][y] = 1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    cnt = 0
    stack = []
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if data[i][j] == 1 and not visited[i][j]:
                stack.append([i, j])
                cnt += 1
                while stack:
                    cur = stack.pop()
                    if not visited[cur[0]][cur[1]]:
                        visited[cur[0]][cur[1]] = 1
                        for dir in range(4):
                            ii, jj = cur[0] + dy[dir], cur[1] + dx[dir]
                            if 0 <= ii < n and 0 <= jj < m and data[ii][jj] == 1 and not visited[ii][jj]:
                                stack.append([ii, jj])
    print(cnt)
