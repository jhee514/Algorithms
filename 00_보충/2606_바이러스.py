import sys

sys.stdin = open("input_2606.txt", "r")


def find(m, data):
    q = []
    visited = [0] * (n + 1)

    curr = 1
    q.append(curr)
    visited[curr] = 1
    while q:
        curr = q.pop(0)
        visited[curr] = 1
        for i in range(m):
            if data[i][0] == curr and not visited[data[i][1]]:
                q.append(data[i][1])
            if data[i][1] == curr and not visited[data[i][0]]:
                q.append(data[i][0])
    cnt = 0
    for i in range(n + 1):
        if visited[i]:
            cnt += 1

    return cnt - 1


n = int(input())
m = int(input())
data = [list(map(int, input().split())) for _ in range(m)]
print(find(m, data))