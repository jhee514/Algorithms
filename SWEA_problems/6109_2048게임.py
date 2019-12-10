import sys

sys.stdin = open("input_6109.txt", "r")


# 0 이 아닌 수들을 차례로 나열
# 그 리스트에서
# 앞에서 부터 같으면 더해서 하나의 수로 만들고
# 다르면 그냥 두고
# 정리되 리스트를 차례로 판에다 다시 입력

# def find():
#     result = [[0]*n for _ in range(n)]
#     if dir == "up":
#         for i in range(n):
#             nums = []
#             for j in range(n):
#                 if data[j][i] != 0:
#                     nums.append(data[j][i])
#             added = add(nums)
#             for l in range(len(added)):
#                 result[l][i] = added.pop(0)
#     elif dir == "left":
#         for i in range(n):
#             nums = []
#             for j in range(n):
#                 if data[i][j] != 0:
#                     nums.append(data[i][j])
#             added = add(nums)
#             for l in range(len(added)):
#                 result[i][l] = added.pop(0)
#     elif dir == "down":
#         for i in range(n):
#             nums = []
#             for j in range(1, n+1):
#                 if data[-j][i] != 0:
#                     nums.append(data[-j][i])
#             added = add(nums)
#             for l in range(1, len(added)+1):
#                 result[-l][i] = added.pop(0)
#     elif dir == "right":
#         for i in range(n):
#             nums = []
#             for j in range(1, n+1):
#                 if data[i][-j] != 0:
#                     nums.append(data[i][-j])
#             added = add(nums)
#             for l in range(1, len(added)+1):
#                 result[i][-l] = added.pop(0)
#     return result


def add(list):
    k = 0
    while k < len(list) - 1:
        if list[k] == list[k + 1]:
            list[k] += list.pop(k + 1)
        k += 1
    return list


T = int(input())
for tc in range(T):
    num, dir = input().split()
    n = int(num)
    data = [list(map(int, input().split())) for _ in range(n)]
    result = [[0] * n for _ in range(n)]
    if dir == "up":
        for i in range(n):
            nums = []
            for j in range(n):
                if data[j][i] != 0:
                    nums.append(data[j][i])
            added = add(nums)
            for l in range(len(added)):
                result[l][i] = added.pop(0)
    elif dir == "left":
        for i in range(n):
            nums = []
            for j in range(n):
                if data[i][j] != 0:
                    nums.append(data[i][j])
            added = add(nums)
            for l in range(len(added)):
                result[i][l] = added.pop(0)
    elif dir == "down":
        for i in range(n):
            nums = []
            for j in range(1, n + 1):
                if data[-j][i] != 0:
                    nums.append(data[-j][i])
            added = add(nums)
            for l in range(1, len(added) + 1):
                result[-l][i] = added.pop(0)
    elif dir == "right":
        for i in range(n):
            nums = []
            for j in range(1, n + 1):
                if data[i][-j] != 0:
                    nums.append(data[i][-j])
            added = add(nums)
            for l in range(1, len(added) + 1):
                result[i][-l] = added.pop(0)

    print("#{}".format(tc + 1))
    for r in result:
        print(' '.join(map(str, r)))
