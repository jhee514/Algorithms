import sys
import time

sys.stdin = open("input_1974.txt", "r")

start = time.time()


def find():
    nine_set = set([i for i in range(1, 10)])
    for i in range(9):
        nums = data[i]
        if set(nums) != nine_set:
            return 0
        nums = [data[j][i] for j in range(9)]
        if set(nums) != nine_set:
            return 0

    for a in range(3):
        for b in range(3):
            result = []
            for m in range(3 * a, 3 * (a + 1)):
                for n in range(3 * b, 3 * (b + 1)):
                    result.append(data[m][n])
            if set(result) != nine_set:
                return 0
    return 1


T = int(input())
for tc in range(T):
    data = [list(map(int, input().split())) for _ in range(9)]
    print("#{} {}".format(tc + 1, find()))
print("time :", time.time() - start)
