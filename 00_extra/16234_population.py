import sys
sys.stdin = open("input_16234.txt", "r")
# sys.stdout = open("testout.txt", "w")

# # bfs
# # q 에 넣고 visited 처리 해주고
# # while q 나왔을 때 돌아가는 for 문에서도 not visited 만 골라서 시작
# # unions 리스트에 q 를 pop 할 때 마다 append 해서 해당 리스트에 담긴 애들의 평균을 내서 인구를 재배치
# # 이 전체 과정을 while 문에 넣어서 인구 차이가 해당 범위 있을 때만 while 에 들어가도록 함수 만들기
#
# # 전체 array 에 해당 범위만큼 인구차이가 나는 국가가 있는지 없는지 체크
#
# import copy
#
# def isgap(data):
#     dx = [0, 0, -1, 1]
#     dy = [1, -1, 0, 0]
#     for i in range(n):
#         for j in range(n):
#             cur = [i, j]
#             for dir in range(4):
#                 y, x = cur[0] + dy[dir], cur[1] + dx[dir]
#                 if 0 <= y < n and 0<= x < n and l <= abs(data[y][x]-data[i][j]) <= r:
#                     return True
#     else:
#         return False
#
# def isstart(data, visited):
#     dx = [0, 0, -1, 1]
#     dy = [1, -1, 0, 0]
#     for i in range(n):
#         for j in range(n):
#             if not visited[i][j]:
#                 start = [i, j]
#                 for dir in range(4):
#                     y, x = start[0] + dy[dir], start[1] + dx[dir]
#                     if 0 <= y < n and 0 <= x < n and l <= abs(data[y][x] - data[i][j]):
#                         return start
#     else:
#         return False
#
# def total_popul(data, countries):
#     total = 0
#     for c in countries:
#         total += data[c[0]][c[1]]
#     return total
#
#
# def find(data, count = 0):
#     dx = [0, 0, -1, 1]
#     dy = [1, -1, 0, 0]
#     # while isgap():
#     visited = [[0] * n for _ in range(n)]
#     result = copy.deepcopy(data)
#     while isstart(data, visited):
#         count += 1
#         unions = []
#         q = []
#         # 옆에 애들이랑 인구차이가 범위사이인 애 + not visited 인 요소를 하나 찾기
#         start = isstart(data, visited)  # [i, j]
#         q.append(start)
#         visited[start[0]][start[1]] = 1
#         while q:
#             cur = q.pop(0)
#             unions.append(cur)
#             # 네 방향 둘러 보고 rightgap(a, b) 일 때 + not visited 일 때
#             for dir in range(4):
#                 y, x = cur[0] + dy[dir], cur[1] + dx[dir]
#                 if 0 <= y < n and 0 <= x < n and l <= abs(data[y][x] - data[cur[0]][cur[1]]) <= r and not visited[y][x]:
#                     # q 에 append + visited == 1
#                     q.append([y, x])
#                     visited[y][x] = 1
#         # q 가 끝나면 해당 unions 의 인구를 분배 시켜서 재배치를 새로운 판 result 에 재배치(=>deepcoyp)
#         for uni in unions:  # [i, j]
#             result[uni[0]][uni[1]] = total_popul(data, unions) // len(unions)
#
#     if isgap(result):
#         return find(result)
#     else:
#         return count
#
#
# # n, l, r = map(int, input().split())
# # data = [list(map(int, input().split())) for _ in range(n)]
# # print(find())
#
# T = 5
# for tc in range(T):
#     n, l, r = map(int, input().split())
#     data = [list(map(int, input().split())) for _ in range(n)]
#     print(find(data))

##########################################################################################################
#
#
# import copy
#
# def isstart(data, visited):
#     dx = [0, 0, -1, 1]
#     dy = [1, -1, 0, 0]
#     for i in range(n):
#         for j in range(n):
#             if not visited[i][j]:
#                 start = [i, j]
#                 for dir in range(4):
#                     y, x = start[0] + dy[dir], start[1] + dx[dir]
#                     if 0 <= y < n and 0 <= x < n and l <= abs(data[y][x] - data[i][j]) <= r and not visited[y][x]:
#                         return start
#     else:
#         return False
#
# def new_p(data, countries):
#     total = 0
#     for c in countries:
#         total += data[c[0]][c[1]]
#     return total // len(countries)
#
# def find(data, count = 0):
#     dx = [0, 0, -1, 1]
#     dy = [1, -1, 0, 0]
#     visited = [[0] * n for _ in range(n)]
#     result = copy.deepcopy(data)
#     start = isstart(data, visited)
#     if start != False:
#         count += 1
#         while start != False:
#             unions = []
#             q = []
#             q.append(start)
#             visited[start[0]][start[1]] = 1
#             while q:
#                 cur = q.pop(0)
#                 unions.append(cur)
#                 for dir in range(4):
#                     y, x = cur[0] + dy[dir], cur[1] + dx[dir]
#                     if 0 <= y < n and 0 <= x < n and l <= abs(data[y][x] - data[cur[0]][cur[1]]) <= r and not visited[y][x]:
#                         q.append([y, x])
#                         visited[y][x] = 1
#             new_popul = new_p(data, unions)
#             for uni in unions:
#                 result[uni[0]][uni[1]] = new_popul
#             start = isstart(data, visited)
#         return find(result, count)
#     else:
#         return count
#
# for tc in range(5):
#     n, l, r = map(int, input().split())
#     data = [list(map(int, input().split())) for _ in range(n)]
#     print(find(data))

######################################################################################################################

import copy

def isstart(data, visited):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                start = [i, j]
                for dir in range(4):
                    y, x = start[0] + dy[dir], start[1] + dx[dir]
                    if 0 <= y < n and 0 <= x < n and l <= abs(data[y][x] - data[i][j]) <= r and not visited[y][x]:
                        return start
    else:
        return False

def new_p(data, countries):
    total = 0
    for c in countries:
        total += data[c[0]][c[1]]
    return total // len(countries)


def find(data, count = 0):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    visited = [[0] * n for _ in range(n)]
    result = copy.deepcopy(data)
    start = isstart(data, visited)

    if start != False:
        count += 1
        v = 0
        while start != False:
            v += 1
            unions = []
            q = []
            q.append(start)
            visited[start[0]][start[1]] = v
            while q:
                cur = q.pop(0)
                unions.append(cur)
                for dir in range(4):
                    y, x = cur[0] + dy[dir], cur[1] + dx[dir]
                    if 0 <= y < n and 0 <= x < n and l <= abs(data[y][x] - data[cur[0]][cur[1]]) <= r and not \
                    visited[y][x]:
                        q.append([y, x])
                        visited[y][x] = v
            new_popul = new_p(data, unions)

            for uni in unions:
                result[uni[0]][uni[1]] = new_popul
            start = isstart(data, visited)
        return find(result, count)
    else:
        return count

for tc in range(5):
    n, l, r = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    print(find(data))