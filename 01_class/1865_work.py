import sys

sys.stdin = open("input_1865.txt", "r")
import time

start = time.time()


def perm(k, temp=100):
    global max
    if k == n:
        if temp > max:
            max = temp

    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            if temp * data[k][arr[k]] > max:
                perm(k + 1, temp * data[k][arr[k]])
            arr[k], arr[i] = arr[i], arr[k]


T = int(input())
for tc in range(T):
    n = int(input())
    arr = [ii for ii in range(n)]
    data = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            data[i][j] *= 0.01
    max = 0
    perm(0)
    print("#%d %.6f" % (tc+1, max))
    # print("time :", time.time() - start)
