import sys

sys.stdin = open("input_1961.txt", "r")


# 90도
def ninety(data):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][-1 - i] = data[i][j]
    return result


# 180도
def oneeighty(data):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[-i - 1][-j - 1] = data[i][j]
    return result


# 270도
def twosenventy(data):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[-j - 1][i] = data[i][j]
    return result


# def rotate(data):
#     nine = ninety(data)
#     eight = oneeighty(data)
#     seven = twosenventy(data)

T = int(input())
for tc in range(T):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    nine = ninety(data)
    eight = oneeighty(data)
    seven = twosenventy(data)
    print("#{}".format(tc + 1))
    for i in range(n):
        print("{} {} {}".format(''.join(map(str, nine[i])), ''.join(map(str, eight[i])), ''.join(map(str, seven[i]))))
