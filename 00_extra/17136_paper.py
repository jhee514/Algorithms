import sys
sys.stdin = open("input_17136.txt", "r")

"""
dfs
    max_size = 0
    max_point = [10, 10]
    최대 정사각형 찾기:
    for i in range(n):
        for j in range(n):
            1 인 점을 찾으면 거기서 가로, 세로 중 짧은 애를 size 로 정하고 이걸 max_size 랑 비교
            이 ㄸㅐ 비지트 처리 해줘서 나중에 같은 사이즈 사각형 나오면 비지트가 적은 애를 먼저 제거 해
    max square =>  
     
재귀
"""
"""
paper = [0, 5, 5, 5, 5, 5]
if any:
0. candidate = []
1. for i in range(n):
        for j in range(n):
        if data[i][j] == 1:
            cur = [i, j]
                while [i][[cut[1]] != 0 or [cur[0]][j] != 0:
                    i += 1
                    j += 1
                size = abs(i - cur[0]
            candidate.append(cur, size)
2. candidate.sort
3. 가장 큰 값이 5보다 작으면 그냥 해당 크기의 색종이 카운팅 -1 해주고 해당 범위의 데이터 0으로 바꿔버려
    else:
        5보다 큰 값이 나오면..........어디를 덮어 줘야 할 지 골라야 하는데 ,,,,
"""

"""
dfs + comb
1 이 나오면 종이를 사이즈별로 덮고 보는데,
    이때, 덮고 싶은 사이즈의 종이가 남아 있어야
최종적으로 판 위에 0 이 있으면 안되고
    0 밖에 없을 때 사용한 종이의 개수(원래 총 개수 - 현재 남은 총 개수)가 최소여 6
"""
def comb():


for _ in range(9):
    tc = int(input())
    data = [list(map(int, input().split())) for _ in range(10)]
    paper = [0, 5, 5, 5, 5, 5]
    for i in range(10):
        for j in range(10):
            if data[i][j] == 1:
                k = 0




#########################################################################
# for _ in range(9):
#     tc = int(input())
#     data = [list(map(int, input().split())) for _ in range(10)]
#
#     paper = [0, 5, 5, 5, 5, 5]
#     cnt = 0
#     visited = [[0] * 10 for _ in range(10)]
#     while sum(map(sum, data)) > 0:
#         candidate = []
#         for i in range(10):
#             for j in range(10):
#                 if data[i][j] == 1:
#                     cur = [i, j]
#                     k = 1
#                     while 0<= cur[0]+k < 10 and 0 <= cur[1] + k < 10:
#                         flag = True
#                         for jj in range(j, cur[1] + k + 1):
#                             if data[cur[0]+k][jj] != 1:
#                                 flag = False
#                         for ii in range(i, cur[0]+k):
#                             if data[cur[0]+k]
#                             data[cur[0]][cur[1] + k] != 0 and data[cur[0]+k][cur[1]] != 0:
#                         k += 1
#                     if k > 0:
#                         candidate.append([cur, k])
#
#         candidate.sort(key=lambda x:x[1], reverse=True)
#         start = candidate[0][0]
#
#         if candidate[0][1] < 6:
#             max_size = candidate[0][1]
#         else:
#             max_size = 5
#
#         # for ii in range(max_size):
#         #     for jj in range(max_size):
#         #         data[start[0] + ii][start[1] + jj] = 0
#
#
#         if paper[max_size] > 0:
#             paper[max_size] -= 1
#             cnt += 1
#         else:
#             cnt = -1
#             break
#
#
#
#     print(tc, cnt)
#     print()
#     for kk in range(10):
#         print(visited[kk])
#     print()
########################################################################
# for _ in range(9):
#     tc = int(input())
#     data = [list(map(int, input().split())) for _ in range(10)]
#
#     paper = [0, 5, 5, 5, 5, 5]
#     cnt = 0
#     while sum(map(sum, data)) > 0:
#         candidate = []
#         for i in range(10):
#             for j in range(10):
#                 if data[i][j] == 1:
#                     cur = [i, j]
#                     k = 1
#                     while 0<= cur[0]+k < 10 and 0 <= cur[1] + k < 10 and data[cur[0]][cur[1] + k] != 0 and data[cur[0]+k][cur[1]] != 0:
#                         k += 1
#                     if k > 0:
#                         candidate.append([cur, k])
#
#         candidate.sort(key=lambda x:x[1], reverse=True)
#         start = candidate[0][0]
#
#         if candidate[0][1] < 6:
#             max_size = candidate[0][1]
#         else:
#             max_size = 5
#
#         for ii in range(max_size):
#             for jj in range(max_size):
#                 data[start[0] + ii][start[1] + jj] = 0
#
#         if paper[max_size] > 0:
#             paper[max_size] -= 1
#             cnt += 1
#         else:
#             cnt = -1
#             break
#     print(tc, cnt)

