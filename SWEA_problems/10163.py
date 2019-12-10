import sys
sys.stdin = open("input_10163.txt", "r")

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
table = [[0]*101 for _ in range(101)]

for i in range(n):
    x = data[i][0]
    y = data[i][1]
    w = data[i][2]
    h = data[i][3]

    for j in range(w):
        for k in range(h):
            table[x+j][y+k] = i + 1

cnt = {}.fromkeys(range(1, n+1), 0)

for z in range(n):
    cnt = 0
    for l in range(101):
        for m in range(101):
            if table[l][m] == z + 1:
                cnt += 1
    print(cnt)