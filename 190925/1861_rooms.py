import sys

sys.stdin = open("input_1861.txt", "r")


def ispath(a, b, cur):
    if 0 <= a < n and 0 <= b < n and data[cur[0]][cur[1]] + 1 == data[a][b]:
        return True


T = int(input())
for tc in range(T):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    result = []
    max_visit = 0
    min_num = 1000000
    checked = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not checked[i][j]:
                stack = [[i, j]]
                visited = [[0] * n for _ in range(n)]
                visited[i][j] = 1
                while stack:
                    cur = stack.pop(-1)
                    checked[cur[0]][cur[1]] = 1
                    for dir in range(4):
                        a, b = cur[0] + dy[dir], cur[1] + dx[dir]
                        if ispath(a, b, cur):
                            stack.append([a, b])
                            visited[a][b] = visited[cur[0]][cur[1]] + 1
                            if visited[a][b] > max_visit:
                                max_visit = visited[a][b]
                                min_num = data[i][j]
                            elif visited[a][b] == max_visit and data[a][b] < min_num:
                                min_num = data[i][j]
    print("#{} {} {}".format(tc + 1, min_num, max_visit))
