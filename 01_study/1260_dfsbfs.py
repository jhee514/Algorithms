import sys

sys.stdin = open("input_1260.txt", "r")

def dfs(data):
    stack = [v]
    visited = [0] * (n+1)
    while stack:
        cur = stack.pop()
        if not visited[cur]:
            print(cur, end=' ')
            visited[cur] = 1
            temp = []
            for ii in range(m):
                if data[ii][0] == cur and not visited[data[ii][1]]:
                    temp.append(data[ii][1])
                elif data[ii][1] == cur and not visited[data[ii][0]]:
                    temp.append(data[ii][0])
            temp.sort(reverse=True)
            stack += temp


def bfs(data):
    q = [v]
    visited = [0] * (n + 1)
    visited[v] = 1
    while q:
        cur = q.pop(0)
        print(cur, end=' ')
        temp = []
        for ii in range(m):
            if data[ii][0] == cur and not visited[data[ii][1]]:
                temp.append(data[ii][1])
                visited[data[ii][1]] = 1
            elif data[ii][1] == cur and not visited[data[ii][0]]:
                temp.append(data[ii][0])
                visited[data[ii][0]] = 1
        temp.sort()
        q += temp


# for _ in range(3):
n, m, v = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(m)]
dfs(data)
print()
bfs(data)
print()
