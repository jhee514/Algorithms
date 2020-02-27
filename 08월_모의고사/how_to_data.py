import sys
sys.stdin = open("input_atom2.txt", 'r')
import time
start = time.time()

################################################################
# time : 0.0009982585906982422
#
# T = int(input())
# for tc in range(T):
#     n = int(input())
#     data = [list(map(int, input().split())) for _ in range(n)]
#     print(data)
# print("time :", time.time() - start)

################################################################
# time : 0.000762939453125

T = int(input())
for tc in range(T):
    n = int(input())
    raw = [list(map(int, input().split())) for _ in range(n)]
    data = [[0]*5 for _ in range(n)]
    for r in range(n):
        data[r][0] = raw[r][0]
        data[r][1] = raw[r][1]
        data[r][4] = raw[r][3]
        if raw[r][2] == 0:
            data[r][2], data[r][3] = 0, 1
        elif raw[r][2] == 1:
            data[r][2], data[r][3] = 0, -1
        elif raw[r][2] == 2:
            data[r][2], data[r][3] = -1, 0
        elif raw[r][2] == 3:
            data[r][2], data[r][3] = 1, 0
    print(data)
print("time :", time.time() - start)