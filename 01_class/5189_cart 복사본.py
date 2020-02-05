import sys

sys.stdin = open("input_5189.txt", "r")

def perm_cart(k):
    global min
    if k == n - 1:
        dist = 0
        dist += data[0][office[0]]
        dist += data[office[n - 2]][0]
        for i in range(n - 2):
            dist += data[office[i]][office[i + 1]]
        if dist < min:
            min = dist
    else:
        for i in range(k, n - 1):
            office[i], office[k] = office[k], office[i]
            perm_cart(k + 1)
            office[i], office[k] = office[k], office[i]


T = int(input())
for tc in range(T):
    n = int(input())
    office = [i for i in range(1, n)]
    min = 100 * n
    data = [list(map(int, input().split())) for _ in range(n)]
    perm_cart(0)
    print("#{} {}".format(tc + 1, min))
