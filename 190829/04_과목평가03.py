import sys

sys.stdin = open("input_quest03.txt", "r")


def island(y, x):
    if 0 <= x < n and 0 <= y < n and data[y][x] != 0:
        return True
    else:
        return False


def find():
    # dfs
    # 일단 시작점을 찾아 cnt += 1
    # 8 가지 방향의 다음 요소가 island() 일 때 + not visited 인 요소만
    # stack 에 넣고 visited 처리 해준다.
    # stack 이 빌 때 까지 영역을 표시를 해 준다.
    # not visited 인 다음 스타팅 포인트를 찾아서 같은 일 반복

    s = []
    visited = [[0] * n for _ in range(n)]
    dx = [0, 0, -1, 1, 1, -1, 1, -1]
    dy = [1, -1, 0, 0, 1, -1, -1, 1]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if data[i][j] != 0 and not visited[i][j]:
                s.append([i, j])
                cnt += 1
                while s:
                    curr = s.pop(-1)
                    a = curr[0]
                    b = curr[1]
                    visited[a][b] = 1

                    for k in range(8):
                        if island(a + dy[k], b + dx[k]) and not visited[a + dy[k]][b + dx[k]]:
                            s.append([a + dy[k], b + dx[k]])
                            visited[a + dy[k]][b + dx[k]] = 1
    return cnt


T = int(input())
for t in range(T):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    print("#{} {}".format(t + 1, find()))
