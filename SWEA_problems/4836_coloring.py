import sys
sys.stdin = open("input_coloring.txt", "r")

T = int(input())
for i in range(T):
    blocks = int(input())
    arr = [[0 for _ in range(10)] for _ in range(10)]
    color = [[0 for _ in range(5)] for _ in range(blocks)]

    for b in range(blocks):
        block = list(map(int, input().split()))
        color[b] = block

    for i in range(len(color)):
        for x in range(color[i][0], color[i][2] + 1):
            for y in range(color[i][1], color[i][3] + 1):
                arr[x][y] += color[i][4]

    count = 0
    for a in range(10):
        for b in range(10):
            if arr[a][b] == 3:
                count += 1

    print("#%d %d" % (i+1, count))