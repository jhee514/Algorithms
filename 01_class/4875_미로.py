import sys
sys.stdin = open("input_4875.txt", "r")

def ispath(i, j):
    if 0 <= i < n and 0 <= j < n and arr[i][j] != 1:
        return True
    else:
        return False


def start(arr):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                return [i, j]


def find(arr):
    s = []
    visited = [[0] * n for _ in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    s.append(start(arr))
    while s:
        curr = s.pop(-1)
        visited[curr[0]][curr[1]] = 1
        x = curr[0]
        y = curr[1]
        for i in range(4):
            if ispath(x + dx[i], y + dy[i]) and not visited[x + dx[i]][y + dy[i]]:
                if arr[x + dx[i]][y + dy[i]] == 3:
                    return 1
                else:
                    s.append([x+dx[i], y+dy[i]])
    return 0

T = int(input())
for t in range(T):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    print("#{} {}".format(t + 1, find(arr)))
