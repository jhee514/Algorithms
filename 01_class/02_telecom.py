import sys

sys.stdin = open("input_telecom.txt", "r")


def isnotwall(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    else:
        return False

def find():
    covered = [[0] * n for _ in range(n)]
    tower = {"A": 2, "B": 3, "C": 4}
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for i in range(n):
        for j in range(n):
            if data[i][j] != "X":
                if data[i][j] in tower.keys():
                    for k in range(tower[data[i][j]]):
                        for l in range(4):
                            if isnotwall(i + dy[l] * k, j + dx[l] * k):
                                covered[i + dy[l] * k][j + dx[l] * k] = 1
    cnt = 0
    for i in range(n):
        for j in range(n):
            if data[i][j] == "H":
                if not covered[i][j]:
                    cnt += 1
    return cnt


T = int(input())
for t in range(T):
    n = int(input())
    data = [list(input()) for _ in range(n)]
    print("#{} {}".format(t + 1, find()))
