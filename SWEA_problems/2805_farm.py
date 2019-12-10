import sys
import time

sys.stdin = open("input_2805.txt", "r")

start = time.time()

T = int(input())
for tc in range(T):
    n = int(input())
    data = [list(map(int, input())) for _ in range(n)]
    total = 0
    total += sum(data[n // 2])
    for i in range(1, n // 2 + 1):
        for j in range(0 + i, n - i):
            total += data[n // 2 + i][j]
            total += data[n // 2 - i][j]
    print("#{} {}".format(tc + 1, total))
print("time :", time.time() - start)
