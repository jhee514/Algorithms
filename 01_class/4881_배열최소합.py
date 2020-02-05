import sys
sys.stdin = open("input_4881.txt", "r")
import time

start = time.time()


def perm(k, r, temp=0):
    global minsum
    if k == r:
        if temp < minsum:
            minsum = temp
    else:
        for j in range(k, n):
            arr[k], arr[j] = arr[j], arr[k]
            if temp + data[k][arr[k]] < minsum:
                perm(k + 1, r, temp + data[k][arr[k]])
            arr[k], arr[j] = arr[j], arr[k]

T = int(input())
for t in range(T):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    arr = [i for i in range(n)]
    minsum = 10 * 10 * 10
    perm(0, n)
    print("#%d %d" % (t + 1, minsum))

##################################################################
# from itertools import permutations
#
# def find():
#     nums = [i for i in range(n)]
#     combis = list(permutations(nums))
#     minsum = 10 * 10 * 10
#     for comb in combis:
#         total = 0
#         for i in range(n):
#             total += data[i][comb[i]]
#             if total > minsum:
#                 break
#         if total < minsum:
#             minsum = total
#     return minsum
#
# T = int(input())
# for t in range(T):
#     n = int(input())
#     data = [list(map(int, input().split())) for _ in range(n)]
#     print("#%d %d" % (t + 1, find()))

print("time :", time.time() - start)
