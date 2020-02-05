import sys
sys.stdin = open("input_5203.txt", "r")

def baby_gin(nums):
    for i in range(len(nums) - 2):
        if nums[i] == nums[i+1] and nums[i+1] == nums[i+2]:
            return True
        elif nums[i] - nums[i+1] == nums[i+1] - nums[i+2] and abs(nums[i+1] - nums[i+2]) == 1:
            return True
    return False

def perm(nums, k, no):
    if k == len(nums):
        if baby_gin(nums):
            result[no] = 1
    else:
        for i in range(k, len(nums)):
            nums[i], nums[k] = nums[k], nums[i]
            perm(nums, k+1, no)
            nums[i], nums[k] = nums[k], nums[i]

def see_result():
    global result
    if result[0] > result[1]:
        return 1
    elif result[0] < result[1]:
        return 2
    elif result[0] == result[1] == 1:
        return 0

T = int(input())
for tc in range(T):
    card = list(map(int, input().split()))
    one = []
    two = []
    result = [0, 0]
    for i in range(6):
        one.append(card[i*2])
        two.append((card[i*2+1]))
        if i > 1:
            perm(one, 0, 0)
            if see_result():
                ans = see_result()
                break
            perm(two, 0, 1)
            if see_result():
                ans = see_result()
                break
    else:
        ans = 0
    print("#{} {}".format(tc+1, ans))
