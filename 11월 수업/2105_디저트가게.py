import sys
sys.stdin = open("2105_input.txt", "r")


# def in_town(i, j):
#     if 0 <= i < n and 0 <= j < n:
#         return True
#
# def is_valid(visited):
#     if visited[0] > 0 and visited[2] > 0 and visited[0] == visited[3] and visited[2] == visited[1]:
#         return True
#
# def find(i, j):
#     global max_dissert
#     dir = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
#     stack = [[i, j]]
#     visited = [[[0]*6]*n for _ in range(n)]
#     visited[i][j] = [0, 0, 0, 0, data[i][j], 1]  # a=0, b=0, c=0, d=0, cnt=0
#     while stack:
#         cur = stack.pop()
#         for d in range(4):
#             y, x = cur[0]+dir[d][0], cur[1]+dir[d][1]
#             if in_town(y, x) and not visited[y][x][5] and data[cur[0]][cur[1]] != data[y][x]:
#                     visited[y][x] = visited[cur[0]][cur[1]]
#                     visited[y][x][d] += 1
#                     visited[y][x][4] += data[y][x]
#                     stack.append([y, x])
#
#     if cur != [i, j] and is_valid(visited[cur[0]][cur[1]]):
#         if visited[cur[0]][cur[1]][4] > max_dissert:
#             max_dissert = visited[cur[0]][cur[1]][4]
#
#
# T = int(input())
# for tc in range(T):
#     n = int(input())
#     data = [list(map(int, input().split())) for _ in range(n)]
#
#     max_dissert = -1
#
#     for i in range(n):
#         for j in range(n):
#             find(i, j)
#     print("#{} {}".format(tc+1, max_dissert))

##############################################################################################
def in_town(i, j):
    if 0 <= i < n and 0 <= j < n:
        return True


def move():
    pass


def find(i, j):
    global max_cnt
    directions = [[(-1, 1), (1, 1),  (1, -1), (-1, -1)],
            [(1, 1), (1, -1), (-1, -1), (-1, 1)],
            [(1, -1), (-1, -1), (-1, 1), (1, 1)],
            [(-1, -1), (-1, 1), (1, 1), (1, -1)]]
    for dir in directions:
        ii, jj = i, j
        for garo in range(1, n+1):
            for sero in range(1, n+1):
                y, x = i, j
                cnt = 0
                visited = [0]*101
                for d in range(4):
                    if d == 0 or d == 3:
                        if in_town(y + dir[d][0]*garo, x + dir[d][1]*garo):
                            g = 1
                            while g <= garo:
                                if not visited[data[y][x]]:
                                    y += dir[d][0]
                                    x += dir[d][1]
                                    visited[data[y][x]] = 1
                                    cnt += 1
                                    g += 1
                                else:
                                    break
                        else:
                            break
                    if d==1 or d==2:
                        if in_town(y+dir[d][0]*sero, x +dir[d][1]*sero):
                            s = 1
                            while s <= sero:
                                if not visited[data[y][x]]:
                                    y += dir[d][0]
                                    x += dir[d][1]
                                    visited[data[y][x]] = 1
                                    cnt += 1
                                    s += 1
                                else:
                                    break
                        else:
                            break
                else:
                    if cnt > max_cnt:
                        max_cnt = cnt


T = int(input())
for tc in range(T):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]

    max_cnt = -1

    for i in range(n):
        for j in range(n):
            find(i, j)
    print("#{} {}".format(tc+1, max_cnt))