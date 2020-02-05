# import sys
#
# # from itertools import combinations
# sys.stdin = open("input_15686.txt", "r")
# #
# # # 치킨집 좌표를 골라서 모아
# # # 집들의 좌표를 골라서 모아
# # # 치킨집에서 m 개를 골라 뽑아
# #     # m 개의 치킨집 조합마다
# #         # 집들의 좌표마다
# #             # m 개의 치킨집 사이 거리를 다 구해서 최솟값 nearest 을 구해
# #         # 이 최솟값의 chicken_distance 을 구해
# #     # 위에서 구한 chicken_distance 의 모음 가운데 가장 작은 최솟값을 구해
# #
# # def findshop(data):
# #     shop = []
# #     for i in range(n):
# #         for j in range(n):
# #             if data[i][j] == 2:
# #                 shop.append([i, j])
# #     return shop
# #
# # def findhouse(data):
# #     house = []
# #     for i in range(n):
# #         for j in range(n):
# #             if data[i][j] == 1:
# #                 house.append([i, j])
# #     return house
# #
# # def howfar(a, b): # a, b 는 각각 리스트로 받는다
# #     return abs(a[0]-b[0]) + abs(a[1]-b[1])
# #
# #
# # def find():
# #     shops = findshop(data)
# #     houses = findhouse(data)
# #     # 치킨집에서 m 개를 골라 뽑아
# #     # m 개의 치킨집 조합마다
# #         # 집들의 좌표마다
# #             # m 개의 치킨집 사이 거리를 다 구해서 최솟값 nearest 을 구해
# #         # 이 최솟값의 합인 total_distance 을 구해
# #     # 위에서 구한 total_distance 의 모음 가운데 가장 작은 최솟값을 chick_dist 로 구해
# #     pickshops = list(combinations(shops, m))
# #     chicken_distance = n * n
# #     for p in pickshops:  # p 는 m개의 치킨집 조합 하나
# #         total_distance = 0
# #         for h in houses:
# #             nearest = howfar(h, p[0])
# #             for i in range(1, m):
# #                 if howfar(h, p[i]) < nearest:
# #                     nearest = howfar(h, p[i])
# #             total_distance += nearest
# #         if total_distance < chicken_distance:
# #             chicken_distance = total_distance
# #     return chicken_distance
# #
# # n, m = map(int, input().split())
# # data = [list(map(int, input().split())) for _ in range(n)]
# # print(find())
#
# ########################################################################
# from itertools import combinations
#
#
# def findshop(data):
#     shop = []
#     for i in range(n):
#         for j in range(n):
#             if data[i][j] == 2:
#                 shop.append([i, j])
#     return shop
#
#
# def findhouse(data):
#     house = []
#     for i in range(n):
#         for j in range(n):
#             if data[i][j] == 1:
#                 house.append([i, j])
#     return house
#
#
# def howfar(a, b):  # a, b 는 각각 리스트로 받는다
#     return abs(a[0] - b[0]) + abs(a[1] - b[1])
#
#
# def find():
#     shops = findshop(data)
#     houses = findhouse(data)
#     pickshops = list(combinations(shops, m))
#     chicken_distance = n * n * n
#     for p in pickshops:  # p 는 m개의 치킨집 조합 하나
#         total_distance = 0
#         for h in houses:
#             nearest = howfar(h, p[0])
#             for i in range(1, m):
#                 if howfar(h, p[i]) < nearest:
#                     nearest = howfar(h, p[i])
#             total_distance += nearest
#         if total_distance < chicken_distance:
#             chicken_distance = total_distance
#     return chicken_distance
#
# n, m = map(int, input().split())
# data = [list(map(int, input().split())) for _ in range(n)]
# print(find())
#
# #118932kb	200ms

import sys

# from itertools import combinations
sys.stdin = open("input_15686.txt", "r")
#
# # 치킨집 좌표를 골라서 모아
# # 집들의 좌표를 골라서 모아
# # 치킨집에서 m 개를 골라 뽑아
#     # m 개의 치킨집 조합마다
#         # 집들의 좌표마다
#             # m 개의 치킨집 사이 거리를 다 구해서 최솟값 nearest 을 구해
#         # 이 최솟값의 chicken_distance 을 구해
#     # 위에서 구한 chicken_distance 의 모음 가운데 가장 작은 최솟값을 구해
#
# def findshop(data):
#     shop = []
#     for i in range(n):
#         for j in range(n):
#             if data[i][j] == 2:
#                 shop.append([i, j])
#     return shop
#
# def findhouse(data):
#     house = []
#     for i in range(n):
#         for j in range(n):
#             if data[i][j] == 1:
#                 house.append([i, j])
#     return house
#
# def howfar(a, b): # a, b 는 각각 리스트로 받는다
#     return abs(a[0]-b[0]) + abs(a[1]-b[1])
#
#
# def find():
#     shops = findshop(data)
#     houses = findhouse(data)
#     # 치킨집에서 m 개를 골라 뽑아
#     # m 개의 치킨집 조합마다
#         # 집들의 좌표마다
#             # m 개의 치킨집 사이 거리를 다 구해서 최솟값 nearest 을 구해
#         # 이 최솟값의 합인 total_distance 을 구해
#     # 위에서 구한 total_distance 의 모음 가운데 가장 작은 최솟값을 chick_dist 로 구해
#     pickshops = list(combinations(shops, m))
#     chicken_distance = n * n
#     for p in pickshops:  # p 는 m개의 치킨집 조합 하나
#         total_distance = 0
#         for h in houses:
#             nearest = howfar(h, p[0])
#             for i in range(1, m):
#                 if howfar(h, p[i]) < nearest:
#                     nearest = howfar(h, p[i])
#             total_distance += nearest
#         if total_distance < chicken_distance:
#             chicken_distance = total_distance
#     return chicken_distance
#
# n, m = map(int, input().split())
# data = [list(map(int, input().split())) for _ in range(n)]
# print(find())

########################################################################
from itertools import combinations


def find_shop_n_house(data):
    shop = []
    house = []

    for i in range(n):
        for j in range(n):
            if data[i][j] == 2:
                shop.append([i, j])
            elif data[i][j] == 1:
                house.append([i, j])
    return [shop, house]


def howfar(a, b):  # a, b 는 각각 리스트로 받는다
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def find():
    shopnhouse = find_shop_n_house(data)
    shops, houses = shopnhouse[0], shopnhouse[1]
    pickshops = list(combinations(shops, m))
    chicken_distance = n * n * n
    for p in pickshops:  # p 는 m개의 치킨집 조합 하나
        total_distance = 0
        for h in houses:
            nearest = howfar(h, p[0])
            for i in range(1, m):
                if howfar(h, p[i]) < nearest:
                    nearest = howfar(h, p[i])
            total_distance += nearest
        if total_distance < chicken_distance:
            chicken_distance = total_distance
    return chicken_distance

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
print(find())

# 116856 kb
# 216 ms
