import sys

sys.stdin = open("input_rabbit.txt", "r")

# 1 : rabbit
# 2 : rock
# 3 : hunter
# 8 방향 12마리
# 사냥꾼은 대각선 위아래로 있는 토끼를 잡는데 바위가 있으면 찾는걸 멈춘다
# 사냥꾼은 전방향을 본.

# DFS

n = 10
data = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, -1, 1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, 1, -1, -1, 1]


def ispath(y, x):
    if 0 <= y < n and 0 <= x < n and data[y][x] != 2:
        return True
    else:
        return False


# dead rabbits 개수를 세는 거니까 => covered 위치가 1 인 토끼수

# hunter 위치를 stack 에 저장
s = []
for i in range(n):
    for j in range(n):
        if data[i][j] == 3:
            s.append([i, j])

# 사냥꾼마다 사냥 가능한 지역을 표시
covered = [[0] * n for _ in range(n)]
while s:
    curr = s.pop(0)  # [a, b]
    a = curr[0]
    b = curr[1]

    for i in range(8):
        k = 0
        while ispath(a + dy[i] * k, b + dx[i] * k):
            covered[a + dy[i] * k][b + dx[i] * k] = 1
            k += 1

# covered 지역에 위치하는 토끼 수 세기
total_dead = 0
for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            if covered[i][j]:
                total_dead += 1

print(total_dead)
