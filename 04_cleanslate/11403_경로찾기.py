import sys
sys.stdin = open("11403_input.txt", "r")


def bfs(i, j, n, data):
    s = [i]
    visited = [0] * (n+1)
    while s:
        cur = s.pop()
        if not visited[cur]:
            visited[cur] = 1
            for ii in range(n):
                if ii == j and data[cur][j]:
                    return True
                elif data[cur][ii] and not visited[ii]:
                    s.append(ii)
    return False


def sol(n, data):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if bfs(i, j, n, data):
                result[i][j] = 1
    return result


for tc in range(2):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    result = sol(n, data)
    for i in range(n):
        print(' '.join(str(x) for x in result[i]))
