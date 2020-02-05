import sys

sys.stdin = open("input_1486.txt", "r")


# def comb(n, r, arr):
#     global b, min
#     if r == 0:
#         if 0<= sum(temp) - b < min:
#             min = sum(temp) - b
#     elif n < r:
#         return
#     else:
#         temp[r-1] = arr[n-1]
#         comb(n-1, r-1, data)
#         comb(n-1, r, data)
#
# T = int(input())
# for tc in range(T):
#     n, b = map(int, input().split())
#     data = list(map(int, input().split()))
#
#     min = b**n
#     for r in range(n+1):
#         temp = [0] * r
#         comb(n, r, data)
#     print("#{} {}".format(tc+1, min))

#####################################################
def comb(n, r, arr, total):
    global min
    if r == 0:
        if 0 <= total < min:
            min = total
    elif n < r:
        return
    else:
        temp[r - 1] = arr[n - 1]
        if total + temp[r-1] < min:
            comb(n - 1, r - 1, data, total + temp[r - 1])
        comb(n - 1, r, data, total)


T = int(input())
for tc in range(1):
    n, b = map(int, input().split())
    data = list(map(int, input().split()))

    min = 10 ** 10
    for r in range(n + 1):
        temp = [0] * r
        comb(n, r, data, -b)
    print("#{} {}".format(tc + 1, min))
