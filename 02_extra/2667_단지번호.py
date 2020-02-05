import sys

sys.stdin = open("input_2667.txt", "r")


def ishouse(y, x):
    if 0 <= x < n and 0 <= y < n and data[y][x] == 1:
        return True
    else:
        return False


def find():
    s = []
    visited = [[0] * n for _ in range(n)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    complex = 0
    count = [0] * n * n
    for i in range(n):
        for j in range(n):
            if data[i][j] == 1 and not visited[i][j]:
                s.append([i, j])
                complex += 1
                while s:
                    curr = s.pop(-1)
                    a, b = curr[0], curr[1]
                    visited[a][b] = complex
                    count[complex] += 1
                    for k in range(4):
                        if ishouse(a + dy[k], b + dx[k]) and not visited[a + dy[k]][b + dx[k]]:
                            s.append([a + dy[k], b + dx[k]])
                            visited[a + dy[k]][b + dx[k]] = complex
    ascending = count[1:complex + 1]
    ascending.sort()
    result = [complex] + ascending
    return result


T = 1
for t in range(T):
    n = int(input())
    data = [list(map(int, input())) for _ in range(n)]
    for i in find():
        print(i)
