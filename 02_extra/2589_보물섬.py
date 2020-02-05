import sys
import time
sys.stdin = open("input_2589.txt", "r")
start = time.time()

# 동서남북으로 이어진 육지 L 사이에서만 이동 가능
# 이동 한 칸 당 한시간 소요
# 육지 간 최 단 거리 이동 위해서는 지나간 곳 또 못지나가고, 돌아가도 안된다.
# 가장 멀리 갈 수 있는 육지 사이의 거리(이동시 걸리는 시간)을 출력
# BFS
# maxtime = 0으로 설정하고 bfs 로 탐색해 나가면서 maxtime 을 증가시켜주면서

# def find():
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]
#     maxtime = 0
#     checked = [[0] * m for _ in range(n)]
#     for i in range(n):
#         for j in range(m):
#             q = []
#             visited = [[0] * m for _ in range(n)]
#             if data[i][j] == "L" and not checked[i][j]:
#                 checked[i][j] = 1
#                 q.append([i, j])
#                 visited[i][j] = 1
#                 while q:
#                     cur = q.pop(0)
#                     for dir in range(4):
#                         a, b = cur[0] + dy[dir], cur[1] + dx[dir]
#                         if 0 <= a < n and 0 <= b < m and data[a][b] == "L" and not visited[a][b]:
#                             q.append([a, b])
#                             visited[a][b] = visited[cur[0]][cur[1]] + 1
#                 if maxtime < max(map(max, visited)):
#                     maxtime = max(map(max, visited))
#     return maxtime - 1
#
#
# n, m = map(int, input().split())
# data = [list(input()) for _ in range(n)]
# print(find())

# time error 는 dp 나 memoization 을 사용해서 이미 지나간 노드와 현재 노드의 거리는 기록 해놓은 값을 가져오도록 해야
# output == 53

########################################################################################################
q: front, rear
version = > 제일
빠르다

def find():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    maxtime = 0
    checked = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            q = [0] * n * m
            front = -1
            rear = -1

            visited = [[0] * m for _ in range(n)]

            if data[i][j] == "L" and not checked[i][j]:
                checked[i][j] = 1
                visited[i][j] = 1
                rear += 1
                q[rear] = [i, j]

                while front != rear:
                    front += 1
                    cur = q[front]
                    for dir in range(4):
                        a, b = cur[0] + dy[dir], cur[1] + dx[dir]
                        if 0 <= a < n and 0 <= b < m and data[a][b] == "L" and not visited[a][b]:
                            rear += 1
                            q[rear] = [a, b]
                            visited[a][b] = visited[cur[0]][cur[1]] + 1
                if maxtime < max(map(max, visited)):
                    maxtime = max(map(max, visited))
    return maxtime - 1


n, m = map(int, input().split())
data = [list(input()) for _ in range(n)]
print(find())

########################################################################################################
# deque version
# from collections import deque
#
# def find():
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]
#     maxtime = 0
#     checked = [[0] * m for _ in range(n)]
#     for i in range(n):
#         for j in range(m):
#             q = deque([])
#             visited = [[0] * m for _ in range(n)]
#             if data[i][j] == "L" and not checked[i][j]:
#                 checked[i][j] = 1
#                 q.append([i, j])
#                 visited[i][j] = 1
#                 while q:
#                     cur = q.popleft()
#                     for dir in range(4):
#                         a, b = cur[0] + dy[dir], cur[1] + dx[dir]
#                         if 0 <= a < n and 0 <= b < m and data[a][b] == "L" and not visited[a][b]:
#                             q.append([a, b])
#                             visited[a][b] = visited[cur[0]][cur[1]] + 1
#                 if maxtime < max(map(max, visited)):
#                     maxtime = max(map(max, visited))
#     return maxtime - 1
#
#
# n, m = map(int, input().split())
# data = [list(input()) for _ in range(n)]
# print(find())
#
########################################################################################################
# q : front , rear version + deque
#
# from collections import deque
#
# def find():
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]
#     maxtime = 0
#     checked = [[0] * m for _ in range(n)]
#     for i in range(n):
#         for j in range(m):
#             q_ins = [0] * n * m
#             q = deque(q_ins)
#             front = -1
#             rear = -1
#
#             visited = [[0] * m for _ in range(n)]
#
#             if data[i][j] == "L" and not checked[i][j]:
#                 checked[i][j] = 1
#                 visited[i][j] = 1
#                 rear += 1
#                 q[rear] = [i, j]
#
#                 while front != rear:
#                     front += 1
#                     cur = q[front]
#                     for dir in range(4):
#                         a, b = cur[0] + dy[dir], cur[1] + dx[dir]
#                         if 0 <= a < n and 0 <= b < m and data[a][b] == "L" and not visited[a][b]:
#                             rear += 1
#                             q[rear] = [a, b]
#                             visited[a][b] = visited[cur[0]][cur[1]] + 1
#                 if maxtime < max(map(max, visited)):
#                     maxtime = max(map(max, visited))
#     return maxtime - 1
#
# n, m = map(int, input().split())
# data = [list(input()) for _ in range(n)]
# print(find())
#
#####################################################################################
#####################################################################################
