import sys

sys.stdin = open("input_5209.txt", "r")


def perm(k, arr, data, total=0):
    global min_cost
    if k == n:
        if total < min_cost:
            min_cost = total
    else:
        for i in range(k, n):
            arr[i], arr[k] = arr[k], arr[i]
            if total + data[k][arr[k]] < min_cost:
                perm(k + 1, arr, data, total + data[k][arr[k]])
            arr[i], arr[k] = arr[k], arr[i]


T = int(input())
for tc in range(T):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    arr = [i for i in range(n)]
    min_cost = 100 * n
    perm(0, arr, data)
    print("#{} {}".format(tc + 1, min_cost))
