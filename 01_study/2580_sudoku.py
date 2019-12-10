import sys
sys.stdin = open("input_2580.txt", "r")


def garo(a):
    y, x = a[0], a[1]
    nums = 45
    if data[y].count('0') == 1:
        for j in range(9):
            if data[y][j] != '0':
                nums -= int(data[y][j])
        data[y][x] = str(nums)
        return True

def sero(a):
    y, x = a[0], a[1]
    zero = 0
    for i in range(9):
        if data[i][x] == '0':
            zero += 1
    if zero == 1:
        nums = 45
        for ii in range(9):
            if data[ii][x] != '0':
                nums -= int(data[ii][x])
        data[y][x] = str(nums)
        return True

def nemo(a):
    y, x = a[0], a[1]
    start = [(y//3)*3, (x//3)*3]
    zero = 0
    nums = 45
    for ii in range(3):
        for jj in range(3):
            if data[start[0] +ii][start[1]+jj] == '0':
                zero += 1
            elif data[start[0] +ii][start[1]+jj] != '0':
                nums -= int(data[start[0] +ii][start[1]+jj])
    if zero == 1:
        data[y][x] = str(nums)

data = [list(input().split()) for _ in range(9)]
total = 0
for s in range(9):
    total += sum([int(data[s][ss]) for ss in range(9)])

while total < 405:
    for i in range(9):
        for j in range(9):
            if data[i][j] == '0':
                z = [i, j]
                if garo(z):
                    continue
                else:
                    if sero(z):
                        continue
                    else:
                        nemo(z)
    total = 0
    for s in range(9):
        total += sum([int(data[s][ss]) for ss in range(9)])

for ddd in range(9):
    print(' '.join(data[ddd]))

##############################################################


#
# def find():
#     zero = []
#     for i in range(9):
#         for j in range(9):
#             if data[i][j] == '0':
#                 zero.append([i, j])
#     return zero
#
# def garo(a):
#     y, x = a[0], a[1]
#     nums = 45
#     if data[y].count('0') == 1:
#         for j in range(9):
#             if data[y][j] != '0':
#                 nums -= int(data[y][j])
#         data[y][x] = str(nums)
#         return True
#
# def sero(a):
#     y, x = a[0], a[1]
#     zero = 0
#     for i in range(9):
#         if data[i][x] == '0':
#             zero += 1
#     if zero == 1:
#         nums = 45
#         for ii in range(9):
#             if data[ii][x] != '0':
#                 nums -= int(data[ii][x])
#         data[y][x] = str(nums)
#         return True
#
# def nemo(a):
#     y, x = a[0], a[1]
#     start = [(y//3)*3, (x//3)*3]
#     zero = 0
#     nums = 45
#     for ii in range(3):
#         for jj in range(3):
#             if data[start[0] +ii][start[1]+jj] == '0':
#                 zero += 1
#             elif data[start[0] +ii][start[1]+jj] != '0':
#                 nums -= int(data[start[0] +ii][start[1]+jj])
#     if zero == 1:
#         data[y][x] = str(nums)
#
# data = [list(input().split()) for _ in range(9)]
# zero = find()
# visited = [0] * len(zero)
# cnt = len(zero)
# while cnt:
#     temp = []
#     for z in zero:
#         if not visited[zero.index(z)]:
#             if data[z[0]][z[1]] != '0':
#                 visited[zero.index(z)] = 1
#                 cnt -= 1
#             elif data[z[0]][z[1]] == '0':
#                 if garo(z):
#                     visited[zero.index(z)] = 1
#                     cnt -= 1
#                 else:
#                     if sero(z):
#                         visited[zero.index(z)] = 1
#                         cnt -= 1
#                     else:
#                         if nemo(z):
#                             visited[zero.index(z)] = 1
#                             cnt -= 1
#     for t in temp:
#         zero.remove(t)
#
# for ddd in range(9):
#     print(' '.join(data[ddd]))
#
# ##############################################################

# def find():
#     zero = []
#     for i in range(9):
#         for j in range(9):
#             if data[i][j] == '0':
#                 zero.append([i, j])
#     return zero
#
# def garo(a):
#     y, x = a[0], a[1]
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#     if data[y].count('0') == 1:
#         for j in range(9):
#             if data[y][j] != '0':
#                 nums.remove(data[y][j])
#         data[y][x] = nums[0]
#         return True
#
# def sero(a):
#     y, x = a[0], a[1]
#     zero = 0
#     for i in range(9):
#         if data[i][x] == '0':
#             zero += 1
#     if zero == 1:
#         nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#         for ii in range(9):
#             if data[ii][x] != '0':
#                 nums.remove(data[ii][x])
#         data[y][x] = nums[0]
#         return True
#
# def nemo(a):
#     y, x = a[0], a[1]
#     start = [(y//3)*3, (x//3)*3]
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#     for ii in range(3):
#         for jj in range(3):
#             if data[start[0] +ii][start[1]+jj] != '0':
#                 nums.remove(data[start[0] +ii][start[1]+jj])
#             if len(nums) == 1:
#                 data[y][x] = nums[0]
#
# data = [list(input().split()) for _ in range(9)]
# zero = find()
# while zero:
#     temp = []
#     for z in zero:
#         if data[z[0]][z[1]] != '0':
#             temp.append(z)
#         elif data[z[0]][z[1]] == '0':
#             if garo(z):
#                 temp.append(z)
#             else:
#                 if sero(z):
#                     temp.append(z)
#                 else:
#                     if nemo(z):
#                         temp.append(z)
#     for t in temp:
#         zero.remove(t)
#
# for ddd in range(9):
#     print(' '.join(data[ddd]))

#############################################################################
# def find():
#     zero = []
#     for i in range(9):
#         for j in range(9):
#             if data[i][j] == '0':
#                 zero.append([i, j])
#     return zero
#
# def garo(a):
#     y, x = a[0], a[1]
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#     if data[y].count('0') == 1:
#         for j in range(9):
#             if data[y][j] != '0':
#                 nums.remove(data[y][j])
#         data[y][x] = nums[0]
#         return True
#
# def sero(a):
#     y, x = a[0], a[1]
#     zero = 0
#     for i in range(9):
#         if data[i][x] == '0':
#             zero += 1
#     if zero == 1:
#         nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#         for ii in range(9):
#             if data[ii][x] != '0':
#                 nums.remove(data[ii][x])
#         data[y][x] = nums[0]
#         return True
#
# def nemo(a):
#     y, x = a[0], a[1]
#     start = [(y//3)*3, (x//3)*3]
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#     for ii in range(3):
#         for jj in range(3):
#             if data[start[0] +ii][start[1]+jj] != '0':
#                 nums.remove(data[start[0] +ii][start[1]+jj])
#             if len(nums) == 1:
#                 data[y][x] = nums[0]

#
# data = [list(input().split()) for _ in range(9)]
# zero = find()
# while zero:
#     for z in zero:
#         if data[z[0]][z[1]] != '0':
#             zero.remove(z)
#         elif data[z[0]][z[1]] == '0':
#             if not garo(z):
#                 if not sero(z):
#                     nemo(z)
#
# for ddd in range(9):
#     print(' '.join(data[ddd]))

# data = [list(input().split()) for _ in range(9)]
# zero = find()
# while zero:
#     for z in zero:
#         if data[z[0]][z[1]] != '0':
#             zero.remove(z)
#         elif data[z[0]][z[1]] == '0':
#             if garo(z):
#                 zero.remove(z)
#             else:
#                 if sero(z):
#                     zero.remove(z)
#                 else:
#                     nemo(z)
#
# for ddd in range(9):
#     print(' '.join(data[ddd]))




#
#
# def garo():
#     for i in range(9):
#         if data[i].count("0") == 1:
#             nums = [str(num) for num in range(1, 10)]
#             for j in range(9):
#                 if data[i][j] != '0':
#                     nums.remove(data[i][j])
#             data[i][data[i].index('0')] = nums[0]
#
# def sero():
#     for j in range(9):
#         zero = 0
#         for i in range(9):
#             if data[i][j] == '0':
#                 zero += 1
#         if zero == 1:
#             nums = [str(num) for num in range(1, 10)]
#             for i in range(9):
#                 if data[i][j] == '0':
#                     z_idx = i
#                 else:
#                     nums.remove(data[i][j])
#             data[z_idx][j] = nums[0]
#
# def nemo():
#     for i in range(3):
#         for j in range(3):
#             start = [i*3, j*3]
#             nums = [str(num) for num in range(1, 10)]
#             for ii in range(3):
#                for jj in range(3):
#                     if data[start[0] +ii][start[1]+jj] == '0':
#                        zero = [start[0] +ii, start[1]+jj]
#                     else:
#                         nums.remove(data[start[0] +ii][start[1]+jj])
#             if len(nums) == 1:
#                 data[zero[0]][zero[1]] = nums[0]
#
#
# data = [list(input().split()) for _ in range(9)]
# total = 0
# for i in range(9):
#     for j in range(9):
#         total += int(data[i][j])
# while total != 405:
#     garo()
#     sero()
#     nemo()
#     total = 0
#     for ii in range(9):
#         for jj in range(9):
#             total += int(data[ii][jj])
# for ddd in range(9):
#     print(' '.join(data[ddd]))