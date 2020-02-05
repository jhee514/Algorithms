import sys

sys.stdin = open("input_2468.txt", "r")

# 동서남북으로 인접한 지역만 한개의 지역으로 인식
# 높이는 최소 0 최대 100 => 바오는 높이도 0<= rain <= 100
# rain 이 range(0, 101) 도는 동안 issafe 의 개수가 최대 (maxsafe) 를 저장해서 return
def safe_areas(rain):
    stack = []
    visited = [[0] * n for _ in range(n)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if data[i][j] > rain and not visited[i][j]:
                cnt += 1
                stack.append([i, j])
                visited[i][j] = 1
                while stack:
                    cur = stack.pop(-1)
                    for dir in range(4):
                        a, b = cur[0] + dy[dir], cur[1] + dx[dir]
                        if 0 <= a < n and 0 <= b < n and data[a][b] > rain and not visited[a][b]:
                            stack.append([a, b])
                            visited[a][b] = 1
    return cnt


def find():
    maxsafe = 0
    for rain in range(101):
        if maxsafe < safe_areas(rain):
            maxsafe = safe_areas(rain)
    return maxsafe


n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
print(find())
