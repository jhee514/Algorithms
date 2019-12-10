import sys
sys.stdin = open("1868_input.txt", "r")

"""
0 에 연결된 숫자들은 한번에 open 이 되니까 한번클릭
0 에 연결이 안된 숫자들은 다 하나하나 클릭 해줘야 해
for i in range(n):
    for j in range(n):
        if data[i][j] == '*':
            visited[i][j] = -1
        elif data[i][j] == 0:
            dfs로 0 을 찾고 => cnt + 1
                주변에 애들은 다 visited 처리 해주고
                    데이터 값이 0 이면 visited = 1
                    데이터 값이 숫자이면 visited = 2
                cur 의 visited 가 1 이상이면 continue   
"""

def get_zeros():
    for i in range(n):
        for j in range(n):
            if data[i][j] == ".":
                data[i][j] = 0


def get_nums():
    global bomb
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for i in range(n):
        for j in range(n):
            if data[i][j] == ".":
                data[i][j] = 0
            if data[i][j] == '*':
                bomb += 1
                for d in dir:
                    y, x = i + d[0], j + d[1]
                    if 0 <= y < n and 0 <= x < n and data[y][x] != '*':
                        data[y][x] = 1

import collections
def find_deque():
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    visited = [[0] * n for _ in range(n)]
    click = 0
    for i in range(n):
        for j in range(n):
            if data[i][j] == 0 and not visited[i][j]:
                click += 1
                que = []
                q = collections.deque(que)
                q.append([i, j])
                visited[i][j] = 1
                while q:
                    cur = q.popleft()
                    for d in dir:
                        y, x = cur[0] + d[0], cur[1] + d[1]
                        if 0 <= y < n and 0 <= x < n and not visited[y][x]:
                            if data[y][x] == 0:
                                visited[y][x] = 1
                                q.append([y, x])
                            elif data[y][x] == 1:
                                visited[y][x] = 1
    return (click, sum(map(sum, visited)))

def find():
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    visited = [[0]*n for _ in range(n)]
    click = 0
    for i in range(n):
        for j in range(n):
            if data[i][j] == 0 and not visited[i][j]:
                click += 1
                q = [0] * n * n
                front, rear = -1, -1
                rear += 1
                q[rear] = [i, j]
                visited[i][j] = 1
                while front != rear:
                    front += 1
                    cur = q[front]
                    for d in dir:
                        y, x = cur[0] + d[0], cur[1] + d[1]
                        if 0 <= y < n and 0 <= x < n and not visited[y][x]:
                            if data[y][x] == 0:
                                visited[y][x] = 1
                                rear += 1
                                q[rear] = [y, x]
                            elif data[y][x] == 1:
                                visited[y][x] = 1
    return (click, sum(map(sum, visited)))


T = int(input())
for tc in range(T):
    n = int(input())
    data = [list(input()) for _ in range(n)]
    bomb = 0
    get_nums()

    # click, cnt_visited = find()
    click, cnt_visited = find_deque()

    result = n*n - bomb - cnt_visited + click
    print("#{} {}".format(tc+1, result))