import sys

sys.stdin = open("input_5110.txt", "r")
from collections import deque


def bigger_index(l1, l2):
    for i in range(n):
        if l1[i] > l2[0]:
            return i


def find():
    for i in range(1, m):
        if max(nums[0]) > nums[i][0]:
            q = deque(nums[0][:bigger_index(nums[0], nums[i])])
            q.extend(nums[i])
            q.extend(nums[0][i:])
        else:
            q = deque(nums[0])
            q.extend(nums[i])

    result = []
    for i in range(10):
        result.append(q[-1 - i])
    return ' '.join(map(str, result))


T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    nums = [list(map(int, input().split())) for _ in range(m)]
    print("#{} {}".format(tc + 1, find()))

##############################################################################################

# def find():
#     q = deque(nums[0])
#     for i in range(1, m):
#         for j in range(n):
#             if q[j] > nums[i][0]:
#                 for k in range(n):
#                     # TODO 이건 class 선언해서 풀어야. insert 는 오래 걸려
#                     q.insert(j, nums[i][k])
#                     j += 1
#                 break
#         else:
#             q.extend(nums[i])
#     result = []
#     for i in range(10):
#         result.append(q[-1 - i])
#     return ' '.join(map(str, result))
#
# T = int(input())
# for tc in range(T):
#     n, m = map(int, input().split())
#     nums = [list(map(int, input().split())) for _ in range(m)]
#     print("#{} {}".format(tc+1, find()))

##############################################################################################
# def find():
#     q = nums[0]
#     for i in range(1, m):
#         for j in range(n):
#             if q[j] > nums[i][0]:
#                 for k in range(n):
#                     q.insert(j, nums[i][k])
#                     j += 1
#                 break
#         else:
#             q.extend(nums[i])
#     result = []
#     for i in range(10):
#         result.append(q[-1 - i])
#     return ' '.join(map(str, result))
#
# T = int(input())
# for tc in range(T):
#     n, m = map(int, input().split())
#     nums = [list(map(int, input().split())) for _ in range(m)]
#     print("#{} {}".format(tc+1, find()))
