import sys

sys.stdin = open("input_6549.txt", "r")

import time

start = time.time()

# 33%
flag = True
while flag:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        flag = False
        break
    n = arr[0]
    data = arr[1:]

    nums = list(set(data))
    nums.sort()
    max_area = 0

    for num in nums:
        max_width = 0
        i = 0
        while i < n:
            if data[i] >= num:
                j = i
                while j < n and data[j] >= num:
                    j += 1
                if j - i > max_width:
                    max_width = j - i
                i = j
            i += 1
        if max_width * num > max_area:
            max_area = max_width * num
    print(max_area)

# flag = True
# while flag:
#     data = list(map(int, input().split()))
#     if data[0] == 0:
#         flag = False
#         break
#     n = data.pop(0)
#     max_area = 0
#     for i in range(n-1):
#         for j in range(i+1, n):
#             if i <= j:
#                 if max_area < min(data[i:j+1]) * (j-i+1):
#                     max_area = min(data[i:j + 1]) * (j - i + 1)
#     print(max_area)


print("time :", time.time() - start)
