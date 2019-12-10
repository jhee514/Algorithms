import sys

sys.stdin = open("input_2005.txt", "r")

# def pascal():
#     pascal = [0] * n
#     pascal[0] = [1]
#     for i in range(1, n):
#         pascal[i] = [0] * (i + 1)
#         for j in range(i+1):
#             if 0<= j - 1 < i +1:
#                 try:
#                     pascal[i][j] += pascal[i-1][j-1]
#                 except IndexError:
#                     pass
#             if 0<= j < i+1:
#                 try:
#                     pascal[i][j] += pascal[i - 1][j]
#                 except IndexError:
#                     pass
#     for p in pascal:
#         print(' '.join(map(str, p)))
#     return

T = int(input())
for tc in range(T):
    n = int(input())
    pascal = [0] * n
    pascal[0] = [1]
    for i in range(1, n):
        pascal[i] = [0] * (i + 1)
        for j in range(i + 1):
            if 0 <= j - 1 < i + 1:
                try:
                    pascal[i][j] += pascal[i - 1][j - 1]
                except IndexError:
                    pass
            if 0 <= j < i + 1:
                try:
                    pascal[i][j] += pascal[i - 1][j]
                except IndexError:
                    pass
    print("#{}".format(tc + 1))
    for p in pascal:
        print(' '.join(map(str, p)))