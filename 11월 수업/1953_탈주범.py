import sys
sys.stdin = open("1953_input.txt", "r")

# TODO : 상대편에서 받아 줄 수 있는 상황 일 때 만 갈 수 있도록

def bfs(a, b):
    dir = [[0],
           [(-1, 0), (1, 0), (0, -1), (0, 1)],
           [(-1, 0), (1, 0)],
           [(0, -1), (0, 1)],
           [(-1, 0), (0, 1)],
           [(1, 0), (0, 1)],
           [(1, 0), (0, -1)],
           [(-1, 0), (0, -1)]]
    q = [0] * n * m
    visited = [[0]*m for _ in range(n)]
    front, rear = -1, -1
    rear += 1
    q[rear] = [a, b]
    visited[a][b] = 1
    while rear != front:
        front += 1
        cur = q[front]
        if visited[cur[0]][cur[1]] == l:
            continue
        for d in dir[data[cur[0]][cur[1]]]:
            y, x = cur[0] + d[0], cur[1] + d[1]
            if 0 <= y < n and 0 <= x < m and not visited[y][x] and data[y][x]:
                for dd in dir[data[y][x]]:
                    if y + dd[0] == cur[0] and x + dd[1] == cur[1]:
                        rear += 1
                        q[rear] = [y, x]
                        visited[y][x] = visited[cur[0]][cur[1]] + 1
    print("#{} {}".format(tc+1, count(visited)))


def count(arr):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                cnt += 1
    return cnt


T = int(input())
for tc in range(T):
    n, m, r, c, l = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    bfs(r, c)
