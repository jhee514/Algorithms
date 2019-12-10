import sys

sys.stdin = open("input_9663.txt", "r")


def perm(k):
    global cnt
    if k == n:
    #     for p in range(n - 1):
    #         for q in range(p + 1, n):
    #             if abs(p - q) == abs(arr[p] - arr[q]):
    #                 return
        cnt += 1

    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            flag = True
            for kk in range(k):
                if abs(k - kk) == abs(arr[k] - arr[kk]):
                    flag = False
            if flag:
                perm(k + 1)
            arr[k], arr[i] = arr[i], arr[k]


n = int(input())
arr = [i for i in range(n)]
pan = [[0] * n for _ in range(n)]
cnt = 0
perm(0)
print(cnt)

# def perm(k):
#     global cnt
#     if k == n:
#         for p in range(n-1):
#             for q in range(p+1, n):
#                 if abs(p-q) == abs(arr[p]-arr[q]):
#                     return
#         cnt += 1
#         pan = [[0] * n for _ in range(n)]
#         for ii in range(n):
#             pan[ii][arr[ii]] = 1
#             print(pan[ii])
#         print()
#
#     else:
#         for i in range(k, n):
#             arr[k], arr[i] = arr[i], arr[k]
#             if 0 == k:
#                 perm(k + 1)
#             elif 0 < k and abs(arr[k-1] - arr[k]) != 1:
#                 perm(k+1)
#             arr[k], arr[i] = arr[i], arr[k]
#
# n = int(input())
# arr = [i for i in range(n)]
# pan = [[0]*n for _ in range(n)]
# cnt = 0
# perm(0)
# print(cnt)
