import sys
from typing import List

sys.stdin = open("1249_input.txt", "r")

"""
TODO
이동하는 시간은 얼마 안걸린다는 전제 = > 비용이 적게 들면 돌아돌아가도 오케이
    => 최단거리 문제가 아니다 => dfs
하지만 아무리 돌아가도 자기가 온 길은 돌아가면 안되겠지 => path
그러니, 최단거리가 아닌 최소비용 문제로서 => min_cost
깊이 우선 탐색으로 돌아온길만 제외하고 다 가보는 방법을 해야 => 남이 거쳐간 칸 지나가도 ok
"""

"""
min, max 초기값 설정을 제대로 하자
min 은 엄청 크게, max는 엄청 작게 초기값을 잡아
"""

# def sol(i, j, path, total_cost):
#     global min_total, min_cost
#     dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#
#     if [i, j] == [n-1, n-1]:
#         if total_cost <= min_total:
#             min_total = total_cost
#     # if [i, j] == [n-1, n-2] or [i, j] == [n-2, n-1]:
#     #     if total_cost + data[n-1][n-1] <= min_total:
#     #         min_total = total_cost + data[n-1][n-1]
#     else:
#         for d in dir:
#             y, x = i + d[0], j + d[1]
#             if 0 <= y < n and\
#                     0 <= x < n and\
#                     total_cost + data[y][x] <= min_total and\
#                     total_cost + data[y][x] <= min_cost[y][x] and\
#                     [y, x] not in path:
#                 min_cost[y][x] = total_cost + data[y][x]
#                 sol(y, x, path + [[y, x]], total_cost + data[y][x])
#
#
# T = int(input())
# for tc in range(T):
#     n = int(input())
#     data = [list(map(int, input())) for _ in range(n)]
#     min_cost = [[10 * n * n] * n for _ in range(n)]
#     min_total = 10 * n * n
#     sol(0, 0, [[0, 0]], data[0][0])
#     print(min_total)
#
#     import time
#     start = time.time()
#     print("time :", time.time() - start)

##########################################################################################################

def sol(i, j, path, total_cost):
    global min_total, min_cost
    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    if [i, j] == [n - 1, n - 1]:
        if total_cost <= min_total:
            min_total = total_cost
    else:
        for d in dir:
            y, x = i + d[0], j + d[1]
            if 0 <= y < n and 0 <= x < n and total_cost + data[y][x] <= min_total and total_cost + data[y][x] <= \
                    min_cost[y][x] and [y, x] not in path:
                min_cost[y][x] = total_cost + data[y][x]
                sol(y, x, path + [[y, x]], total_cost + data[y][x])


T = int(input())
for tc in range(T):
    n = int(input())
    data = [list(map(int, input())) for _ in range(n)]
    min_cost = [[10 * n * n] * n for _ in range(n)]
    min_total = 10 * n * n
    sol(0, 0, [[0, 0]], data[0][0])
    print("#{} {}".format(tc + 1, min_total))