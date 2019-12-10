# a 1 b 2 c 3 d 4 e 5 f 6
data = [[1, 2, 3], [1, 3, 4], [2, 4, 5], [3, 2, 1], [3, 4, 4], [3, 5, 5], [4, 5, 3], [4, 6, 4], [5, 1, 3], [5, 6, 5]]

arr = [[10000]*7 for _ in range(7)]
for d in data:
    arr[d[0]][d[1]] = d[2]

dis = [[0]*2 for _ in range(7)]

def dijkstra(s, a, d):
    u = {s}

    for v in range(7):
        dis[v][0] = arr[s][v]
    while u:

