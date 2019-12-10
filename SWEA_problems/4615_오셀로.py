import sys

sys.stdin = open("input_4615.txt", "r")


def isrock(table, p, q):
    if 0 <= p < n and 0 <= q < n and table[p][q] != 0:
        return True
    else:
        return False


def find(n):
    table = [[0] * n for _ in range(n)]
    base = [2, 1, 1, 2]
    for i in range(n // 2 - 1, n // 2 + 1):
        for j in range(n // 2 - 1, n // 2 + 1):
            table[i][j] = base.pop(0)
    for turn in data:
        a, b = turn[0] - 1, turn[1] - 1
        table[b][a] = turn[2]
        dy = [1, -1, 0, 0, 1, 1, -1, -1]
        dx = [0, 0, 1, -1, 1, -1, 1, -1]
        for dir in range(8):
            # 8 방향 의 다음 칸에 다른색의 돌이 있는지 찾기
            next_y, next_x = b + dy[dir], a + dx[dir]
            if isrock(table, next_y, next_x) and table[next_y][next_x] != turn[2]:
                z = 2
                while 1:
                    nth_y, nth_x = b + dy[dir] * z, a + dx[dir] * z
                    # nth_y, nth_x =  next_y + dy[dir], next_x + dx[dir]
                    if isrock(table, nth_y, nth_x) and table[nth_y][nth_x] == table[next_y][next_x]:
                        # next_y += dy[dir]
                        # next_x += dx[dir]
                        z = z + 1
                    elif isrock(table, nth_y, nth_x) and table[nth_y][nth_x] == turn[2]:
                        for y in range(z + 1):
                            table[b + dy[dir] * y][a + dx[dir] * y] = turn[2]
                    else:
                        break
            else:
                continue
    result = [0] * 2
    for p in range(n):
        for q in range(n):
            if table[p][q] == 1:
                result[0] += 1
            elif table[p][q] == 2:
                result[1] += 1
    print(table)
    return ' '.join(map(str, result))

T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(m)]
    print("#{} {}".format(tc + 1, find(n)))
