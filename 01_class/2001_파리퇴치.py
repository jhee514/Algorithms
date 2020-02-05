import sys

sys.stdin = open("input_2001.txt", "r")

# 배열에서 MxM 영역들의 합 중 최대값 출려
def find():
    max_dead = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            dead = 0
            for p in range(m):
                for q in range(m):
                    dead += flies[i + p][j + q]
            if dead > max_dead:
                max_dead = dead
    return max_dead

T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(n)]
    print("#{} {}".format((tc + 1), find()))
