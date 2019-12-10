import sys

sys.stdin = open("input_5105.txt", "r")


def ispath(i, j):
    if 0 <= i < n and 0 <= j < n and arr[i][j] != 1 and arr[i][j] != 2:
        return True
    else:
        return False


def start(arr):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                return [i, j]


def find(arr):
    q = []
    visited = [[0] * n for _ in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    q.append(start(arr))
    while q:
        curr = q.pop(0)
        x = curr[0]
        y = curr[1]
        for i in range(4):
            if ispath(x + dx[i], y + dy[i]) and not visited[x + dx[i]][y + dy[i]]:
                q.append([x + dx[i], y + dy[i]])
                visited[x + dx[i]][y + dy[i]] += visited[x][y] + 1
                if arr[x + dx[i]][y + dy[i]] == 3:
                    return visited[x + dx[i]][y + dy[i]] - 1
    return 0

T = int(input())
for t in range(T):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    print("#{} {}".format(t + 1, find(arr)))