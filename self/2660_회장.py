import sys
sys.stdin = open("2660_input.txt", "r")

n = int(input())
data = [[0] * (n+1) for _ in range(n+1)]
for _ in range(n):
    a, b = map(int, input().split())
    if a == -1:
        break
    else:
        data[a][b] = 1
        data[b][a] = 1

# score = [0] * (n+1)

for i in range(1, n+1):
    if sum(data[i]) == n - 1:
        continue
    else:
        for j in range(1, n+1):
            friends = []
            strangers = []
            if j != i and not data[i][j]:
                strangers.append([j])
            elif j != i and data[i][j]:
                friends.append([i])
            while strangers:
                score = 2
                to_be_removed = []
                for f in friends:
                    for s in strangers:
                        if s in friends:
                            continue
                        elif data[f][s] or data[s][f]:
                            data[i][s] = score
                            to_be_removed.append(s)
                            friends.append(f)
                strangers = list(set(strangers) - set(to_be_removed))
                score += 1

"""
data 합이 n - 1 이면 점수가 1
data 가 0 인 곳에서 bfs 해서 depth 구하고 이거의 최대 값이 해당 사람의 score
"""
for d in range(n):
    print(data[d])
print(score)