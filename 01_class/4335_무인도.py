import sys

sys.stdin = open("input_4335.txt", "r")


def find():
    for i in range(n):
        for j in range(n):
            if data[i][j] == 1 or data[i][j] == 2:


T = int(input())
for tc in range(T):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
