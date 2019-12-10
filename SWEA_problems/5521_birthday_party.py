import sys
sys.stdin = open("input_5521.txt", "r")

def dijkstra(s, A, D):
    U = {s}

    for v in range(1, n+1):
        D[v] = A[s][v]

    while U != set(range(1, n+1)):
        min_d = D.index(min(D))
        if min_d not in U:
            U = U + {min_d}
            for

T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    A = [[1000]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        A[a][b] = 1
    D = [0] * (n+1)
    dijkstra(1, A, D)
    print("#{} {}".format(tc+1, cnt))

#######################################################################

# T = int(input())
# for tc in range(T):
#     n, m = map(int, input().split())
#     data = [list(map(int, input().split())) for _ in range(m)]
#
#     visited = [0] * (n+1)
#     q = [1]
#     visited[1] = 1
#     cnt = 0
#     while q:
#         cur = q.pop(0)
#         if 1 < visited[cur] < 4:
#             cnt += 1
#         if visited[cur] < 3:
#             for d in data:
#                 if d[0] == cur and not visited[d[1]]:
#                     q.append(d[1])
#                     visited[d[1]] = visited[cur] + 1
#                 elif d[1] == cur and not visited[d[0]]:
#                     q.append(d[0])
#                     visited[d[0]] = visited[cur] + 1
#
#     print("#{} {}".format(tc+1, cnt))