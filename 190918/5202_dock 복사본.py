import sys

sys.stdin = open("input_5202.txt", "r")

T = int(input())
for tc in range(T):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if data[j][1] < data[min][1]:
                min = j
            elif data[j][1] == data[min][1]:
                if data[j][0] > data[min][0]:
                    min = j
        data[i], data[min] = data[min], data[i]

    visited = [0] * 24
    total = 0
    for ii in range(n):
        if sum(visited[data[ii][0]:data[ii][1]]) == 0:
            for jj in range(data[ii][0], data[ii][1]):
                visited[jj] = 1
            total += 1
    print("#{} {}".format(tc + 1, total))
