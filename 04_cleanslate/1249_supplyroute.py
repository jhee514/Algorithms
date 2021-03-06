import sys
sys.stdin = open("1249_input.txt", "r")

"""
컨설턴트님 팁
가지치기 + 메모이제이션
"""
def in_field(n, a, b):
    if 0 <= a < n and 0<= b < n:
        return True
    else:
        return False

def bfs(n, data):
    from collections import deque
    q = deque()
    q.append((0, 0))
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    min_cost = [[-1] * n for _ in range(n)]
    min_cost[0][0] = 0
    while q:
        cur = q.popleft()
        for d in dir:
            y, x = cur[0] + d[0], cur[1] + d[1]
            if in_field(n, y, x):
                if min_cost[y][x] == -1 or min_cost[y][x] < min_cost[cur[0]][cur[1]] + data[y][x]:
                    min_cost[y][x] = min_cost[cur[0]][cur[1]] + data[y][x]
                    q.append((y, x))
    return min_cost[n-1][n-1]


# def dfs(data):
#     stack = [v]
#     visited = [0] * (n+1)
#     while stack:
#         cur = stack.pop()
#         if not visited[cur]:
#             print(cur, end=' ')
#             visited[cur] = 1
#             temp = []
#             for ii in range(m):
#                 if data[ii][0] == cur and not visited[data[ii][1]]:
#                     temp.append(data[ii][1])
#                 elif data[ii][1] == cur and not visited[data[ii][0]]:
#                     temp.append(data[ii][0])
#             temp.sort(reverse=True)
#             stack += temp


def dfs(n, data):
    min_route = 100000000
    dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    memoization = [[100000]*n for _ in range(n)]
    stack = [[0, 0]]
    visited = [[0]*n for _ in range(n)]

    visited[0][0] = 1
    memoization[0][0] = 0
    while stack:
        cur = stack.pop(-1)
        for d in dir:
            dy, dx = cur[0] + d[0], cur[1] + d[1]
            if in_field(n, dy, dx) and not visited[dy][dx] and memoization[dy][dx] >= memoization[cur[0]][cur[1]] + data[dy][dx]:
                memoization[dy][dx] = memoization[cur[0]][cur[1]] + data[dy][dx]
                stack.append([dy, dx])
                visited[dy][dx] = 1
                if dy == n-1 and dx == n-1 and memoization[n-1][n-1] < min_route:
                    min_route = memoization[n-1][n-1]
    return min_route


T = int(input())
for tc in range(T):
    n = int(input())
    data = [list(map(int, input())) for _ in range(n)]
    print("#{} {}".format(tc+1, bfs(n, data)))
    # print("#{} {}".format(tc+1, dfs(n, data)))