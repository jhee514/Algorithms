import sys

sys.stdin = open("1260_input.txt", "r")

"""
간선은 양쪽에서 봐야한다
"""


def dfs_sol(n, m, v, data):
    s = []
    s.append(v)
    visited = [0] * (n + 1)
    order = []
    while s:
        cur = s.pop()
        temp = []
        if not visited[cur]:
            order.append(cur)
            visited[cur] = 1
            for i in range(m):
                if cur in data[i]:
                    if cur == data[i][0] and not visited[data[i][1]]:
                        temp.append(data[i][1])
                    elif cur == data[i][1] and not visited[data[i][0]]:
                        temp.append(data[i][0])
            if temp:
                temp.sort(reverse=True)
                s += temp
    return ' '.join(str(x) for x in order)


def bfs_sol(n, m, v, data):
    q = []
    q.append(v)
    visited = [0] * (n + 1)
    order = []
    while q:
        cur = q.pop(0)
        temp = []
        if not visited[cur]:
            order.append(cur)
            visited[cur] = 1
            for i in range(m):
                if cur in data[i]:
                    if cur == data[i][0] and not visited[data[i][1]]:
                        temp.append(data[i][1])
                    elif cur == data[i][1] and not visited[data[i][0]]:
                        temp.append(data[i][0])
            if temp:
                temp.sort()
                q += temp
    return ' '.join(str(x) for x in order)


for tc in range(4):
    n, m, v = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(m)]
    print(dfs_sol(n, m, v, data))
    print(bfs_sol(n, m, v, data))
