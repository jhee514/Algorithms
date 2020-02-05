import sys

sys.stdin = open("input_17135.txt", "r")
import time

start = time.time()

from itertools import combinations
import copy


def find_enemy(data):
    enemies = []
    for i in range(n):
        for j in range(m):
            if data[i][j] == 1:
                enemies.append([i, j])
    return enemies


def howfar(a, b):
    return abs(n - b[0]) + abs(a - b[1])


def move(data):
    result = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if data[i][j] == 1:
                if i + 1 < n:
                    result[i + 1][j] = 1
    return result


def ifany(data):
    for i in range(n):
        for j in range(m):
            if data[i][j] == 1:
                return True
    else:
        return False


def pick_nearest(po, enemies):
    min_dis = d + 1
    nearest = [n, m]
    for en in enemies:
        cur_dis = howfar(po, en)
        if cur_dis <= d:
            if cur_dis < min_dis:
                min_dis = cur_dis
                nearest = en
            elif cur_dis == min_dis:
                if nearest[1] > en[1]:
                    nearest = en
    if nearest == [n, m]:
        return None
    else:
        return nearest


def find(game):
    nums = [i for i in range(n)]
    positions = list(combinations(nums, 3))
    max_killed = 0

    for posis in positions:
        data = copy.deepcopy(game)
        cur_killed = 0
        while ifany(data):
            enemies = find_enemy(data)
            to_kill = []
            for po in posis:
                nearest = pick_nearest(po, enemies)
                if nearest != None:
                    to_kill.append(nearest)

            for to in to_kill:
                a, b = to[0], to[1]
                if data[a][b] == 1:
                    data[a][b] = 0
                    cur_killed += 1
            data = move(data)
        if max_killed < cur_killed:
            max_killed = cur_killed
    return max_killed


for tc in range(6):
    n, m, d = map(int, input().split())
    game = [list(map(int, input().split())) for _ in range(n)]
    print(find(game))

print("time :", time.time() - start)
#####################################################################################################################
#
# def find(game):
#     nums = [i for i in range(n)]
#     positions = list(combinations(nums, 3))
#     max_killed = 0
#
#     for posis in positions:
#         data = copy.deepcopy(game)
#         cur_killed = 0
#         while ifany(data):
#             enemies = find_enemy(data)
#             to_kill = []
#             for po in posis:
#                 nearest = pick_nearest(po, enemies)
#                 to_kill.append(nearest)
#             for to in to_kill:
#                 try:
#                     if data[to[0]][to[1]] == 1:
#                         data[to[0]][to[1]] -= 1
#                         cur_killed += 1
#                 except IndexError:
#                     pass
#             data = move(data)
#
#         if max_killed < cur_killed:
#             max_killed = cur_killed
#     return max_killed
#####################################################################################################################

# for tc in range(6):
#     n, m, d = map(int, input().split())
#     data = [list(map(int, input().split())) for _ in range(n)]
#     nums = [i for i in range(n)]
#     positions = list(combinations(nums, 3))  # [(0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 2, 3), (0, 2, 4), (0, 3, 4), (1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
#     max_killed = 0
#     for posis in positions:  # (n1, n2, n3)
#         cur_killed = 0
#         while ifany(data):
#             enemies = find_enemy(data)
#             to_kill = []
#             for po in posis:  # n1 # 궁수마다 제일 가까운 적 고르기
#                 min_dis = 1000
#                 nearest = [n, m]
#                 for en in enemies:  # [y, x] # 적들 가운데 가장 가까운 놈 고르기
#                     cur_dis = howfar(po, en)
#                     if cur_dis <= d:
#                         if cur_dis < min_dis:
#                             min_dis = cur_dis
#                             nearest = en
#                         elif cur_dis == min_dis:
#                             if nearest[1] > en[1]:
#                                 nearest = en
#                 to_kill.append(nearest)
#             for to in to_kill:  # 궁수 셋과 가장 가까운 놈들 다 제거
#                 try:
#                     data[to[0]][to[1]] = 0
#                     cur_killed += 1
#                 except IndexError:
#                     pass
#             data = move(data)  # 적을 한칸씩 옮기고 다시 시작
#         if max_killed < cur_killed:
#             max_killed = cur_killed
#     print(max_killed)
#
# print("time :", time.time() - start)
# 궁수 3 명을 배치
# 각 턴 마다 궁수 각 1 적수를 없애 => 같은 적을 공격 가능
# 공격 받은 적은 0 으로 바꿔 없앤다
# 궁수와 적의 거리가 d 이하
# 적 가운데 가장 가까운 놈
# 거리가까운 놈 여럿이면 가장 왼쪽 놈 공격
# 턴이 끝나면 적은 아래로 한칸 이동
# 모든 적이 마지막 행을 넘어가면 게임 끝
# 궁수를 n 열 가운데 3개 배치하는데 이 중 가장 많은 적을 죽일 수 있는 적의 수를 출력


# 궁수 3을 배치할 조합을 짜내 => # nums = [i for i in range(n)] 에서 positions combinations(nums, 3)
# 적의 위치를 뽑아내
# maxkilled = 0
# for 조합 in 조합s => # for posis in positions:  # posis = (n1, n2, n3)
# while 적이 있는 동안:
# for 궁수 in 궁수s
# min_dis = 100
# for 적 in 적s:  # 젤 왼쪽 놈부터
# if 궁수 에서 적과의 거리가 d 이상이면:
# pass
# else:
# cur_dis < min_dis:
# min_dis = cur_dis
# nearst_enemy.append[적y, 적x]
# nearest 안의 적은 다 없애
# 적들의 위치를 한칸씩 아래로 이동
# max_killed < cur_killed
# max_killed = cur_killed
# 적이 없다면
# return maxkilled
