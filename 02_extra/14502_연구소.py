import copy
import sys

sys.stdin = open("input_14502.txt", "r")


def find_zeroes(data):
    zeroes = []
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                zeroes.append([i, j])
    return zeroes


def three(points):
    p = len(points)
    pos_walls = []
    for i in range(p - 2):
        for j in range(i + 1, p - 1):
            for k in range(j + 1, p):
                pos_walls.append([points[i], points[j], points[k]])
    return pos_walls


def count_safe(data):
    total = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                total += 1
    return total


def find(data):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    safe = []
    # 0 들의 좌표 모임
    zeroes = find_zeroes(infos)
    #  0 의 위치들 가운데 세점을 고른 조합들을 생성
    pos_walls = three(zeroes)
    # 이 조합을 순차적으로 돌면서 조합 안의 좌표들은 1로 바꾸고
    # TODO data의 값이 변해버리잖아

    for walls in pos_walls:  # [walls[0], walls[1], walls[2]] => [y1, x1] ...
        data = copy.deepcopy(infos)
        # 픽 된 조합 안 좌표들을 1로 바꿔
        for w in range(3):
            y, x = walls[w][0], walls[w][1]
            data[y][x] = 1

        #  2 가 동서남북으로 나갈 때 0 을 만나는 동안은 0을 2로 바꾸고, 1을 만나면 멈춘다
        visited = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if data[i][j] == 2 and not visited[i][j]:
                    q = []
                    q.append([i, j])
                    visited[i][j] = 1
                    while q:
                        cur = q.pop(0)
                        for dir in range(4):
                            a, b = cur[0] + dy[dir], cur[1] + dx[dir]
                            if 0 <= a < n and 0 <= b < m and data[a][b] == 0 and not visited[a][b]:
                                q.append([a, b])
                                visited[a][b] = 1
                                data[a][b] = 2
        safe.append(count_safe(data))
    return max(safe)
    #  그런 후 테이블 위의 0 의 개수를 구해야


T = 3
for tc in range(T):
    n, m = map(int, input().split())
    infos = [list(map(int, input().split())) for _ in range(n)]
    print(find(infos))
