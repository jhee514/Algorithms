l = [[2, 1], [3, 0], [3, 0], [9, 8, 2, 1], [5], [7, 6, 4], [7, 5], [6, 5], [3], [3]]


# n = len(l)
# visited = [0] * n
#
#
# def dfs(v):
#     visited[v] = True
#     print(v, ' ', end='')
#     for w in l[v]:
#         if not visited[w]:
#             dfs(w)
#
#
# def bfs(i):
#     q = []
#     visited[i] = True
#     q.append(i)
#     while len(q):
#         v = q.pop(0)
#         print(v, ' ', end='')
#         for w in l[v]:
#             if not visited[w]:
#                 visited[w] = True
#                 q.append(w)
#
# print('DFS 방문 순서:')
# for i in range(n):
#     if not visited[i]:
#         dfs(i)
#
# visited = [0] * n
# print('BFS 방문 순서:')
# for j in range(n):
#     if not visited[j]:
#         bfs(j)

def get_power_set(s):
    power_set = [[]]
    for elem in s:
        # iterate over the sub sets so far
        for sub_set in power_set:
            # add a new subset consisting of the subset at hand added elem
            power_set = power_set + [list(sub_set) + [elem]]
    return power_set


print("get power set: ", get_power_set(l))
