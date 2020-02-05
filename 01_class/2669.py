import sys
sys.stdin = open("input_2669.txt", "r")

data = [list(map(int, input().split())) for _ in range(4)]
table = [[0]*100 for _ in range(100)]

for i in range(4):
    x1 = data[i][0]
    y1 = data[i][1]
    x2 = data[i][2]
    y2 = data[i][3]

    for j in range(x1, x2):
        for k in range(y1, y2):
            table[j][k] = 1

cnt = 0
for p in range(100):
    for q in range(100):
        if table[p][q] == 1:
            cnt += 1
print(cnt)