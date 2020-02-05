import sys
sys.stdin = open("input_3074.txt", "r")

import time
start = time.time()

"""
시간의 최솟값을 구하니까
초 마다 해당 심사대 (걸리는 시간 // cur_time) 의 합을 더해서 이게 총 인구보다 작으면 출력
"""


T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    data = list(int(input()) for _ in range(n))
    min_t = min(data)

    left = 0
    right = min_t * m

    while left < right:
        mid = (right + left) // 2
        finished = sum([mid // d for d in data])
        if finished < m:
            left = mid + 1
        else:
            right = mid
    print("#{} {}".format(tc + 1, left))
#
# # pooh
# TC = int(input())
# for tc in range(1, TC + 1):
#     N, M = map(int, input().split())  # 심사대, 사람
#     desk = [0] * N
#     for i in range(N):
#         desk[i] = int(input())
    # r = min(desk) * M
    # l = min(desk)
    #
    # while l < r:
    #     people = 0
    #     mid = (l + r) // 2
    #     for i in range(N):
    #         people += mid // desk[i]
    #
    #     if people < M:
    #         l = mid + 1
    #     else:
    #         r = mid
    #
    # print("#%d" % tc, l)

# time : 0.00044918060302734375
# 제한시간초과 2개
# T = int(input())
# for tc in range(T):
#     n, m = map(int, input().split())
#     data = list(int(input()) for _ in range(n))
#     min_t = min(data)
#     t = min_t
#     while 1:
#         if sum([t // d for d in data]) >= m:
#             print("#{} {}".format(tc + 1, t))
#             break
#         else:
#             t += 1
print("time :", time.time() - start)
