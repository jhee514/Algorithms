import sys

sys.stdin = open("input_5188.txt", "r")

"""
(0, 0) 에서 시작해서
오른쪽이나 아래칸으로만 이동
dfs
해당 값을 total 에 넣어주고
맨 아랫반복
"""
#  distance 에 요소별 값의 누적 값을 저장

T = int(input())
for tc in range(T):
    n = int(input())
    data = [list(map(int, input().split())) for i in range(n)]

    dir = [(1, 0), (0, 1)]
    stack = [(0, 0)]
    distance = [[0] * n for _ in range(n)]
    distance[0][0] = data[0][0]
    result = []
    while stack:
        cur = stack.pop(-1)
        for d in range(2):
            y = cur[0] + dir[d][0]
            x = cur[1] + dir[d][1]
            if 0 <= y < n and 0 <= x < n:
                if y == (n - 1) and x == (n - 1):
                    result.append((distance[cur[0]][cur[1]] + data[y][x]))
                else:
                    stack.append((y, x))
                    distance[y][x] = distance[cur[0]][cur[1]] + data[y][x]
    print("#{} {}".format(tc + 1, min(result)))

####################################################################################
# 이렇게 하면 안돼!!
# TODO : 왜 이렇게는 안돼??
# while stack:
#         cur = stack.pop(-1)
#         if cur == (n-1, n-1):
#             sum.append(visited[n-1][n-1])
#         for d in range(2):
#             y = cur[0] + dir[d][0]
#             x = cur[1] + dir[d][1]
#             if 0<= y < n and 0<= x < n:
#                 stack.append((y, x))
#                 visited[y][x] = visited[cur[0]][cur[1]] + data[y][x]
