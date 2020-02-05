import sys
sys.stdin = open("input_1931.txt", "r")

# n = int(input())
# data = {}
# for _ in range(n):
#     temp = list(map(int, input().split()))
#     if temp[0] in data.keys():
#         data[temp[0]].append(temp)
#     else:
#         data[temp[0]] = [temp]
# for t in range(24):
#     if t in data.keys() and len(data[t]) > 1:
#         data[t].sort(key=lambda x:x[1])
#
# for tt in range(24):
#     if tt in data.keys():
#         cur = tt
#         break
# visited = [0] * 24
# cnt = 0
# while cur < 24:
#     if cur in data.keys():
#         cnt += 1
#         for ttt in range(data[cur][0][0], data[cur][0][1]):
#             visited[ttt] = 1
#         cur = data[cur][0][1]
#     else:
#         cur += 1
# print(cnt)
#

# for _ in range(2):
# n = int(input())
# data = [list(map(int, input().split())) for _ in range(n)]
# for i in range(n-1):
#     min = i
#     for j in range(i+1, n):
#         if data[j][0] <= data[min][0]:
#             min = j
#     if data[min][0] == data[i][0]:
#         if data[min][1] > data[i][1]:
#             data[i+1], data[min] = data[min], data[i+1]
#         else:
#             data[min], data[i] = data[i], data[min]
#     else:
#         data[min], data[i] = data[i], data[min]
# max_cnt = 0
#
# for t in range(len(data)):
#     cnt = 1
#     finished = data[t][1]
#     for tt in data[t + 1:]:
#         if finished <= tt[0]:
#             cnt += 1
#             finished = tt[1]
#     if cnt > max_cnt:
#         max_cnt = cnt
# print(max_cnt)


for _ in range(2):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    data.sort()

    max_cnt = 0
    for t in range(len(data)):
        cnt = 1
        finished = data[t][1]
        for tt in data[t + 1:]:
            if finished <= tt[0]:
                cnt += 1
                finished = tt[1]
        if cnt > max_cnt:
            max_cnt = cnt
    print(max_cnt)
