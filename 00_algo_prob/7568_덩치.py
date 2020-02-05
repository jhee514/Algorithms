n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
rank = [0] * n
for i in range(n):
    cnt = 1
    for j in range(n):
        if i != j:
            if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
                cnt += 1
    rank[i] = cnt
for r in rank:
    print(r, end=' ')