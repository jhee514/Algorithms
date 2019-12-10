import sys
sys.stdin = open("input_2178.txt", "r")

"""
bfs 로 가는데,
visited 에 이동한 칸 수를 저장하게 된다
"""
T = 4
for _ in range(T):
    n, m = int(input().split())
    data = [list(map(int, input())) for _ in range(n)]


    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    q = [0] * n * m
    front = -1
    rear = -1
    visited = [[0] * m for _ in range(n)]

    rear += 1
    q[rear] = [0, 0]
    visited[0][0] = 1
    while q:
        front += 1
        cur = q.pop(front)
        for vector in range(4):
            y, x = cur[0] + directions[vector][0], cur[1] + directions[vector][1]
            if 0 <= y < n and 0<= x < m and data[y][x] == 1 and not visited[x][y]:
                rear += 1
                q[rear] = [y, x]
                visited[y][x] = visited[cur[0]]visited[cur[1]] + 1




