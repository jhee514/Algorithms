import sys

sys.stdin = open("input_ant.txt", "r")


def isexit(x, y):
    if x < 0 or x > n - 1 or y > n - 1 or y < 0:
        return True
    else:
        return False


def find():
    cnt = 0
    # 상0 하1 좌2 우3
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    dir = 3
    x, y = 0, 0
    while not isexit(x + dx[dir], y + dy[dir]):
        y = y + dy[dir]
        x = x + dx[dir]
        cnt += 1
        if data[y][x] == 1:
            if dir == 0:
                dir = 3
            elif dir == 1:
                dir = 2
            elif dir == 2:
                dir = 1
            elif dir == 3:
                dir = 0
        if data[y][x] == 2:
            if dir == 0:
                dir = 2
            elif dir == 1:
                dir = 3
            elif dir == 2:
                dir = 0
            elif dir == 3:
                dir = 1
    else:
        return cnt


T = int(input())
for t in range(T):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    print(find())
