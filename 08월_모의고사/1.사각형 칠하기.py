import sys

sys.stdin = open("sample_input.txt", 'r')


def find(data):
    color_cnt = [0] * 11
    table = [[0] * m for _ in range(n)]

    for i in range(k):
        a = data[i][0]
        b = data[i][1]
        c = data[i][2]
        d = data[i][3]
        color = data[i][4]

        current_color = []
        for p in range(a, c + 1):
            for q in range(b, d + 1):
                current_color.append(table[p][q])
        if max(current_color) <= color:
            for t in range(a, c + 1):
                for u in range(b, d + 1):
                    table[t][u] = color
    for r in range(n):
        for s in range(m):
            color_cnt[table[r][s]] += 1
    return max(color_cnt)


T = int(input())
for t in range(T):
    n, m, k = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(k)]
    print("#%d %d" % (t + 1, find(data)))
