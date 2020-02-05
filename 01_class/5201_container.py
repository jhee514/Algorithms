import sys
sys.stdin = open("input_5201.txt", "r")

"""
하나의 짐이 하나의 트럭과 짝을 짓는데
짐이 용량보다 작아야
1. 모든 조합을 뽑아서 각각의 트럭용량과 짐 무게를 비교
2. ...
"""
import time
start = time.time()

# def comb(data, n, r):
#     global cnt
#     if r == 0:
#         perm_truck(0, m, m, temp)
#     elif n < r:
#         return
#     else:
#         temp[r-1] = data[n-1]
#         comb(data, n-1, r-1)
#         comb(data, n-1, r)
#
#
# def perm_truck(k, n, m, data):
#     global max_load
#     if k == n:
#         total = 0
#         for kk in range(k):
#             if truck[kk] >= data[kk]:
#                 total += data[kk]
#         if total > max_load:
#             print(total)
#             max_load = total
#     else:
#         for i in range(k, m):
#             truck[i], truck[k] = truck[k], truck[i]
#             perm_truck(k+1, n, m, data)
#             truck[i], truck[k] = truck[k], truck[i]
#
#
# T = int(input())
# for tc in range(T):
#     n, m = map(int, input().split())
#     container = list(map(int, input().split()))
#     truck = list(map(int, input().split()))
#     max_load = 0
#
#     if n > m:
#         temp = [0] * m
#         comb(container, n, m)
#     else:
#         perm_truck(0, n, m, container)
#     print("#{} {}".format(tc+1, max_load))
#
#     print("time :", time.time() - start)
#############################################################################

T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    container_raw = list(map(int, input().split()))
    truck_raw = list(map(int, input().split()))

    container = sorted(container_raw, reverse=True)  # container_raw.sorted(reverse=True)
    truck = sorted(truck_raw, reverse=True)
    if n > m:
        cnt = m
    if n <= m:
        cnt = n
    c = -1
    total = 0
    used = [0] * m
    while cnt:  # while i < m and j < n:
        c += 1
        if c == n:
            break
        for t in range(m):
            if truck[t] >= container[c] and not used[t]:
                total += container[c]
                used[t] = 1
                cnt -= 1
                break
    print("#{} {}".format(tc+1, total))
    print("time :", time.time() - start)