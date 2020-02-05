import sys

sys.stdin = open("input_1247.txt", "r")

import time

start = time.time()


def perm(k):
    n = 0
    global result

    if k == N:
        total = 0
        for i in range(N):
            # print(t[i], end=" ")
            total += distance[n][t[i] + 1]
            n = t[i] + 1
        total += distance[n][1]
        # print(total)
        if result > total:
            result = total
        # print()
    else:
        for i in range(N):
            if visited[i]:
                continue
            else:
                t[k] = arr[i]
                visited[i] = 1
                perm(k + 1)
                visited[i] = 0


for tc in range(1, 1 + int(input())):
    N = int(input())
    info = list(map(int, input().split()))

    place = []
    for i in range(0, len(info), 2):
        place.append((info[i], info[i + 1]))

    # print(place)

    distance = [[0] * (N + 2) for i in range(N + 2)]

    for i in range(N + 2):
        for j in range(N + 2):
            distance[i][j] = abs(place[i][0] - place[j][0]) + abs(place[i][1] - place[j][1])
    # print(distance)

    # ttl = 0
    result = 200 * (N + 2)

    arr = [i for i in range(1, N + 1)]
    t = [0] * N
    visited = [0] * N
    perm(0)
    print('#%d %d' % (tc, result))
print("time :", time.time() - start)
