raw = 1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7
data = list(raw[i*2:(i+1)*2] for i in range(len(raw)//2))

print("recursive")
def bfs(a):
    q = []
    q.append(a)
    while q:
        cur = q.pop(0)
        if not r_visit[cur]:
            print(cur, end=' ')
            r_visit[cur] = 1
            for j in range(len(data)):
                if data[j][0] == cur and not r_visit[data[j][1]]:
                    q.append(data[j][1])
                elif data[j][1] == cur and not r_visit[data[j][0]]:
                    q.append(data[j][0])


r_visit = [0] * 8
bfs(1)

print()
print("while")


q = []
visited = [0] * 8
q.append(1)
visited[1] = 1
while q:
    cur = q.pop(0)
    print(cur, end=' ')
    for j in range(len(data)):
        if data[j][0] == cur and not visited[data[j][1]]:
            q.append(data[j][1])
            visited[data[j][1]] = 1
        elif data[j][1] == cur and not visited[data[j][0]]:
            q.append(data[j][0])
            visited[data[j][0]] = 1