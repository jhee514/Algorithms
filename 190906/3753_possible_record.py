import sys

sys.stdin = open("input_3753.txt", "r")
# sys.stdout = open("textout.txt", "w")

"""
set 에는 tuple, string 만 들어 갈 수 있다
"""

import time

start = time.time()

# ##############################################################################

# # from itertools import combinations
# #
# # T = int(input())
# # for tc in range(T):
# #     n = int(input())
# #     data = list(map(int, input().split()))
# #     records = []
# #     for i in range(n+1):
# #         temp = list(combinations(data, i))
# #         for j in temp:
# #             if sum(j) not in records:
# #                 records.append(sum(j))
# #     print("#{} {}".format(tc+1, len(records)))
# ##############################################################################
# # time : 6.320965766906738
#
# # from itertools import combinations
# #
# # T = int(input())
# # for tc in range(T):
# #     n = int(input())
# #     data = list(map(int, input().split()))
# #     records = []
# #     for i in range(n + 1):
# #         temp = list(combinations(data, i))
# #         for j in temp:
# #             records.append(sum(j))
# #             records = list(set(records))
# #     print("#{} {}".format(tc + 1, len(records)))
#
# ##############################################################################
#
# ##############################################################################
# # time : 7.7630650997161865
# # time : 1.8353137969970703
# # time : 0.002257823944091797
#
# def powersetlist(data):
#     comb = []
#     records = {}
#     for e in data:
#         temp = [x + e for x in comb]
#         for i in range(len(temp)):
#             records.add(sum(temp[i]))
#             # print(comb)
#
#         comb += temp
#         comb = set(comb)
#
#         # print(comb)
#     return len(records)
#
# #############################################################################################
# # 0.00031280517578125
#
# T = int(input())
# for tc in range(T):
#     n = int(input())
#     data = list(map(int, input().split()))
#
#     comb = [[]]
#     records = {sum(comb[0])}
#     for d in data:
#         temp = [x + [d] for x in comb]
#         for i in temp:
#             # records.add(sum(i))
#             if i not in comb:
#                 comb.append(i)
#     for j in comb:
#         records.add(sum(j))
#     print("#{} {}".format(tc + 1, len(records)))
#     # powersetlist(data)
#
# #############################################################################################

# T = int(input())
# for tc in range(T):
#     n = int(input())
#     data = list(map(int, input().split()))
#     print(data)
#     scores = [0]
#     for i in data:
#         temp = []
#         for j in scores:
#             s = i + j
#             temp.append(s)
#         scores += temp
#         scores = list(set(scores))
#     print("#{} {}".format(tc + 1, len(scores)))

# #############################################################################################
# time : 0.0008702278137207031

T = int(input())
for tc in range(T):
    n = int(input())
    data = list(map(int, input().split()))
    scores = [0]
    for i in data:
        for j in range(len(scores)):
            scores.append(i + j)
        scores = list(set(scores))
    print("#{} {}".format(tc + 1, len(scores)))
print("time :", time.time() - start)