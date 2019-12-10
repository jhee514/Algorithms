import sys

sys.stdin = open("input_1541.txt", "r")
"""
연산자에 대한 순열?
"""

"""
최솟값을 필요
- 뒤 숫자가 최대여야
- 전후로 숫자를 먼저 연산 시키고
다 빼줘
"""

data = input()
operator = ['-', '+']
nums = []
temp = 0
flag = False
for i in range(len(data)):
    if i == len(data) - 1:
        if flag == True:
            nums[-1] += int(data[temp:])
        elif flag == False:
            nums.append(int(data[temp:]))
    elif data[i] in operator:
        if flag == True:
            nums[-1] += int(data[temp:i])
            temp = i + 1
        elif flag == False:
            nums.append(int(data[temp:i]))
            temp = i + 1
        if data[i] == operator[1]:
            flag = True
        if data[i] == operator[0]:
            flag = False
result = nums[0]
for iii in range(1, len(nums)):
    result -= nums[iii]
print(result)
