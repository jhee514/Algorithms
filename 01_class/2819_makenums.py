import sys

sys.stdin = open("input_2819.txt", "r")


def pick_num(k, n):
    global cnt
    comb = [0] * 7
    if k == n:
        temp = ''
        for j in range(7):
            temp += nums[comb[j]]
        result.append(temp)
    else:
        for i in range(l):
            comb[k] = i
            pick_num(k+1,  n)


T = int(input())
for tc in range(T):
    data = [list(map(str, input().split())) for _ in range(4)]

    nums = []
    for i in range(4):
        for j in range(4):
           nums.append(data[i][j])
    nums = list(set(nums))
    print(nums)
    l = len(nums)
    cnt = 7
    result = []
    pick_num(0, cnt)
    result = set(result)

    print(result)