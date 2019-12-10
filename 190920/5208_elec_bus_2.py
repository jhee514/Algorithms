import sys

sys.stdin = open("input_5208.txt", "r")

"""
1번 배터리는 무조건 장착
"""
def comb():
    if r == 0:

    elif n < r:
        return

    else:
        t[r-1] = a[n-1]
        comb(n-1, r-1)
        comb(n-1, r)


T = int(input())
for tc in range(T):
    data = list(map(int, input().split()))
    arr = list(range(n))

    print("#{} {}".format(tc + 1, cnt - 1))

######################################################
# T = int(input())
# for tc in range(T):
#     data = list(map(int, input().split()))
#     arr = data[0]
#     cnt = 0
#     cur = 1
#     while arr > 1:
#         if arr - cur <= data[cur]:
#             arr = cur
#             cur = 1
#             cnt += 1
#         else:
#             cur += 1
#     print("#{} {}".format(tc + 1, cnt - 1))
