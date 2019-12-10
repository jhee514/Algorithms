import sys

sys.stdin = open("input_magnetic.txt", "r")


def find(arr):
    cnt = 0
    for j in range(n):
        nexti = 0
        for i in range(nexti, n - 1):
            if arr[i][j] == 1:
                nexti = i + 1
                while nexti < 99 and arr[nexti][j] == 0:
                    nexti += 1
                if arr[nexti][j] == 2:
                    cnt += 1
                    nexti += 1
    return cnt


T = 10
for t in range(T):
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(100)]
    print("#%d %d" % (t + 1, find(table)))
