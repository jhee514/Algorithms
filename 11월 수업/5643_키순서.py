import sys
sys.stdin = open("5643_input.txt", "r")
"""
checked 를 n+1 * n+1 만큼 만들어서
각각의 정보가 들어올 때마다 1 처리를 해주고
각각에 대해서 dfs로 확인하는데 이때, 
    나보다 작은 놈은 걔보다 작은 놈들만 dfs
    나보다 큰 놈은 걔보다 큰놈만 dfs

"""



# T = int(input())
# for tc in range(T):
#     n = int(input())
#     m = int(input())
#     # data = [list(map(int, input().split())) for _ in range(m)]
#
#     checked = [[0]*(n+1) for _ in range(n+1)]
#
#     for i in range(m):
#         a, b = map(int, input().split())
#         checked[a][b] = 1
#
#     # dfs
#     cnt = 0
#     for stu in range(1, n+1):  # cur = ii
#         bigger_stack = []
#         smaller_stack = []
#         visited = [0] * (n+1)
#         visited[stu] = 1
#         for ii in range(1, n+1):
#             if not visited[ii]:
#                 if checked[stu][ii] == 1:
#                     bigger_stack.append(ii)
#                     visited[ii] = 1
#                     while bigger_stack:
#                         cur = bigger_stack.pop()
#                         for j in range(1, n+1):
#                             if checked[cur][j] == 1 and not visited[j]:
#                                 bigger_stack.append(j)
#                                 visited[j] = 1
#                 elif checked[ii][stu] == 1:
#                     smaller_stack.append(ii)
#                     visited[ii] = 1
#                     while smaller_stack:
#                         cur = smaller_stack.pop()
#                         for jj in range(1, n+1):
#                             if checked[jj][cur] == 1 and not visited[jj]:
#                                 smaller_stack.append(jj)
#                                 visited[jj] = 1
#         if sum(visited) == n:
#             cnt += 1
#     print("#{} {}".format(tc+1, cnt))
#
# # output: 1

T = int(input())
for tc in range(T):
    n = int(input())
    m = int(input())
    checked = [[0]*(n+1) for _ in range(n+1)]
    for i in range(m):
        a, b = map(int, input().split())
        checked[a][b] = 1

    cnt = 0
    for stu in range(1, n+1):  # cur = ii
        visited = [0] * (n+1)
        visited[stu] = 1
        for ii in range(1, n+1):
            if not visited[ii]:
                if checked[stu][ii] == 1:
                    stack = [ii]
                    visited[ii] = 1
                    while stack:
                        cur = stack.pop()
                        for j in range(1, n+1):
                            if checked[cur][j] == 1 and not visited[j]:
                                stack.append(j)
                                visited[j] = 1
                elif checked[ii][stu] == 1:
                    stack = [ii]
                    visited[ii] = 1
                    while stack:
                        cur = stack.pop()
                        for jj in range(1, n+1):
                            if checked[jj][cur] == 1 and not visited[jj]:
                                stack.append(jj)
                                visited[jj] = 1
        if sum(visited) == n:
            cnt += 1
    print("#{} {}".format(tc+1, cnt))
