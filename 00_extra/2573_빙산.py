import sys
sys.stdin = open("input_2573.txt", "r")


def isocean(arr, y, x):
    if 0 <= y < n and 0 <= x < m and arr[y][x] == 0:
        return True
    else:
        return False

def isice(arr, y, x):
    if 0 <= y < n and 0 <= x < m and arr[y][x] > 0:
        return True
    else:
        return False

def cnt_icebergs(arr):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    stack = []
    visited = [[0] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0 and not visited[i][j]:
                stack.append([i, j])
                cnt += 1
                while stack:
                    curr = stack.pop(-1)
                    a, b = curr[0], curr[1]
                    visited[a][b] = 1
                    for d in range(4):
                        y, x = a + dy[d], b + dx[d]
                        if isice(arr, y, x) and not visited[y][x]:
                            stack.append([y, x])
                            visited[y][x] = 1
    return cnt

def find(data, years=0):
    years += 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    later = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if data[i][j] > 0:
                surrounded = 0
                for dir in range(4):
                    p, q = i + dy[dir], j + dx[dir]
                    if isocean(data, p, q):
                        surrounded += 1
                if data[i][j] > surrounded:
                    later[i][j] = data[i][j] - surrounded
                elif data[i][j] <= surrounded:
                    later[i][j] = 0
    if cnt_icebergs(later) == 0:
        return 0
    elif cnt_icebergs(later) > 1:
        return years
    elif cnt_icebergs(later) == 1:
        return find(later, years)

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
if cnt_icebergs(data) == 1:
    print(find(data))
else:
    print(0)
