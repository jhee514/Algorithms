import sys

sys.stdin = open("input_6485.txt", "r")

def find():
    bus_stop = [0] * 5001
    for i in range(n):
        for j in range(data[i][0], data[i][1] + 1):
            bus_stop[j] += 1
    result = []
    for k in range(p):
        result.append(bus_stop[c[k]])
    return ' '.join(map(str, result))

T = int(input())
for tc in range(T):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    p = int(input())
    c = [int(input()) for _ in range(p)]
    print("#{} {}".format(tc + 1, find()))