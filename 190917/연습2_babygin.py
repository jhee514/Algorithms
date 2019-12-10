def perm(nums, k):
    if k == n:
        if baby_gin(nums):
            print("baby-gin :", nums)
            return
    else:
        for i in range(k, n):
            nums[i], nums[k] = nums[k], nums[i]
            perm(nums, k+1)
            nums[i], nums[k] = nums[k], nums[i]

def baby_gin(nums):
    cnt = 0

    for i in range(2):
        if nums[i*3] - nums[i*3+1] == 0 and nums[i*3+1] - nums[i*3+2] == 0:
            cnt += 1
        elif nums[i*3] - nums[i*3+1] == nums[i*3+1] - nums[i*3+2]:
            cnt += 1
    if cnt == 2:
        return True
    else:
        return False

data = [[1, 2, 4, 7, 8, 3], [6, 6, 7, 7, 6, 7], [0, 5, 4, 0, 6, 0], [1, 0, 1, 1, 2, 3]]
n = 6
for d in data:
    perm(d, 0)