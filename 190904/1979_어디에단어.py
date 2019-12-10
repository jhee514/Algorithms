import sys

sys.stdin = open("input_1979.txt", "r")


def find():
    result = 0
    for i in range(n):
        if sum(data[i]) >= k:
            j = 0
            while j < n:
                if data[i][j] == 1:
                    cnt = 1
                    j += 1
                    while 0 <= j < n and data[i][j] == 1:
                        cnt += 1
                        j += 1
                    if cnt == k:
                        result += 1
                else:
                    j += 1
    for i in range(n):
        j = 0
        while j < n:
            if data[j][i] == 1:
                cnt = 1
                j += 1
                while 0 <= j < n and data[j][i] == 1:
                    cnt += 1
                    j += 1
                if cnt == k:
                    result += 1
            else:
                j += 1
    return result

T = int(input())
for tc in range(T):
    n, k = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    print("#{} {}".format(tc + 1, find()))