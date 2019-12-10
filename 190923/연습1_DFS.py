raw = 1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7
"""
인접리스트를 사용하면 코드가 훨씬 깔끔해진다
"""
def dfs(a):
    print(a, end=' ')
    visited[a] = 1
    for i in range(len(data)):
        if data[i][0] == a and not visited[data[i][1]]:
            dfs(data[i][1])
        elif data[i][1] == a and not visited[data[i][0]]:
            dfs(data[i][0])

data = list(raw[i*2:(i+1)*2] for i in range(len(raw)//2))
stack = []
visited = [0] * 8
vvisited = [0] * 8
stack.append(1)
while stack:
    cur = stack.pop(-1)
    if not vvisited[cur]:
        vvisited[cur] = 1
        print(cur, end=' ')
        for i in range(len(data)):
            if data[i][0] == cur and not vvisited[data[i][1]]:
                stack.append(data[i][1])
            elif data[i][1] == cur and not vvisited[data[i][0]]:
                stack.append(data[i][0])
# vvisited[1] = 1
# while stack:
#     cur = stack.pop(-1)
#     print(cur, end=' ')
#     for i in range(len(data)):
#         if data[i][0] == cur and not vvisited[data[i][1]]:
#             stack.append(data[i][1])
#             vvisited[data[i][1]] = 1
#         elif data[i][1] == cur and not vvisited[data[i][0]]:
#             stack.append(data[i][0])
#             vvisited[data[i][0]] = 1

print()
dfs(1)
