import sys
sys.stdin = open("input_1244.txt", "r")
import copy
# def perm(k, arr):
#     global mx_p
#     if k == r:
#         result = int(''.join(arr))
#         if result > mx_p:
#             mx_p = result
#     else:
#         if k > n - 1:
#             kk = k - n + 1
#         else:
#             kk = k
#         for i in range(n):
#             if i != kk:
#                 arr[i], arr[kk] = arr[kk], arr[i]
#                 perm(k+1, arr)
#                 arr[i], arr[kk] = arr[kk], arr[i]

# def perm(k, arr):
#     global mx_p
#     if k == r:
#         result = int(''.join(arr))
#         if result > mx_p:
#             mx_p = result
#     else:
#         for i in range(n):
#             for j in range(n):
#                 if i != j:
#                     arr[i], arr[j] = arr[j], arr[i]
#                     perm(k+1, arr)
#                     arr[i], arr[j] = arr[j], arr[i]
#
# T = int(input())
# for tc in range(T):
#     a, b = input().split()
#     data = list(a)
#     n = len(data)
#     r = int(b)
#     mx_p = 0
#     perm(0, data)
#     print("#{} {}".format(tc+1, mx_p))
"""
큰 값은 앞으로 빼 주는데,
큰 값 중 idx 이 큰 애(제일 뒤에 있는)를 가져와서 바꾸고

"""


# T = int(input())
# for tc in range(T):
#     a, b = input().split()
#     data = list(a)
#     n = len(data)
#     cnt = int(b)
#
#     print(''.join(data), cnt)
#
#     for i in range(n-1):
#         max = i
#         for j in range(i+1, n):
#             if int(data[max]) <= int(data[j]):
#                 max = j
#         if max != i:
#             data[i], data[max] = data[max], data[i]
#             cnt -= 1
#
#             print(''.join(data), cnt)
#
#         if cnt == 0:
#             break
#
#     print(''.join(data), cnt)
#
#     if cnt % 2:
#         for ii in range(n):
#             if data.count(data[ii]) > 1:
#                 print("#{} {}".format(tc + 1, ''.join(data)))
#                 break
#         else:
#             data[-1], data[-2] = data[-2], data[-1]
#             print("#{} {}".format(tc + 1, ''.join(data)))
#     else:
#         print("#{} {}".format(tc+1, ''.join(data)))

###################################################################
# def perm(k, r, arr):
#     # backtracking => 이미 최대 상금이고 남은 횟수가 짝수인 경우 멈추도록
#     global mx_p, max_arr
#     if arr == sorted_data and (r - k) % 2 == 0:
#         mx_p = int(''.join(arr))
#         return
#     if k == r:
#         if int(''.join(arr)) > mx_p:
#             mx_p = int(''.join(arr))
#     else:
#         for i in range(k, n):
#             if i != k:
#                 arr[i], arr[k] = arr[k], arr[i]
#                 perm(k+1, r, arr)
#                 arr[i], arr[k] = arr[k], arr[i]
#
# T = int(input())
# for tc in range(T):
#     a, b = input().split()
#     data = list(a)
#
#     sorted_data = copy.deepcopy(data)
#     sorted_data.sort(reverse=True)
#     maximum = int(''.join(sorted_data))
#
#     n = len(data)
#     cnt = int(b)
#     mx_p = 0
#
#     if cnt < n+1 :
#         perm(0, cnt, data)
#         print("#{} {}".format(tc + 1, mx_p))
#
#     else:
#         perm(0, n, data)
#         print(tc+1, mx_p)
#         if (cnt-n) % 2:
#             for ii in range(n):
#                 if data.count(data[ii]) > 1:
#                     print("#{} {}".format(tc + 1, mx_p))
#                     break
#             else:
#                 max_arr = list(str(mx_p))
#                 max_arr[-1], max_arr[-2] = max_arr[-2], max_arr[-1]
#                 print("#{} {}".format(tc + 1, ''.join(max_arr)))
#         else:
#             print("#{} {}".format(tc + 1, ''.join(data)))

###########################################################################
def perm(k, r, arr):
    # backtracking => 이미 최대 상금이고 남은 횟수가 짝수인 경우 멈추도록
    global mx_p, max_arr
    if arr == sorted_data and (r - k) % 2 == 0:
        mx_p = int(''.join(arr))
        return
    if k == r:
        if int(''.join(arr)) > mx_p:
            mx_p = int(''.join(arr))
    else:
        for i in range(k, n):
            if i != k:
                arr[i], arr[k] = arr[k], arr[i]
                perm(k+1, r, arr)
                arr[i], arr[k] = arr[k], arr[i]

def comb_r(k, s):
    if k == R: print(t[0], t[1])
    else:
        for i in range(s, N + (k - R) + 1):
            t[k] = a[i]
            comb_r(k + 1, i + 1)

T = int(input())
for tc in range(T):
    a, b = input().split()
    data = list(a)

