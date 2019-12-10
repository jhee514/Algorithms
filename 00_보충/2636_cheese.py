import sys

sys.stdin = open("input_2636.txt", "r")


def morethanzero(arr):
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0:
                return True
    else:
        return False


def count_cheese(data):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == 1:
                cnt += 1
    return cnt


def ischeese(data, y, x):
    if 0 <= y < n and 0 <= x < m and data[y][x] == 1:
        return True
    else:
        return False


def iszero(data, y, x):
    if 0 <= y < n and 0 <= x < m and data[y][x] == 0:
        return True
    else:
        return False


def find(data, hours=0):
    hours += 1
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    air = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    stack = [[0, 0]]
    visited[0][0] = 1
    air[0][0] = 1
    while stack:
        curr = stack.pop(-1)
        a, b = curr[0], curr[1]
        for dir in range(4):
            y, x = a + dy[dir], b + dx[dir]
            if iszero(data, y, x) and not visited[y][x]:
                stack.append([y, x])
                visited[y][x] = 1
                air[y][x] = 1

    hour_later = [[0] * m for _ in range(n)]
    for c in range(n):
        for d in range(m):
            if data[c][d] == 1:
                for dir in range(4):
                    p, q = c + dy[dir], d + dx[dir]
                    if iszero(data, p, q) and air[p][q]:
                        hour_later[c][d] = 0
                        break
                else:
                    hour_later[c][d] = 1
    if morethanzero(hour_later):
        return find(hour_later, hours)
    else:
        print(hours)
        return count_cheese(data)

n, m = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(n)]
print(find(cheese))