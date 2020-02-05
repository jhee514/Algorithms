nums = [1, 2, 3, 4]
num = [4]
# print(list(set(nums)-set(num)))


def for_perm(r, k=0):
    if k == r:
        print(arr)
    else:
        for i in range(4):
            arr[k] = nums[i]
            for_perm(r, k+1)

r = 5
arr = [0] * r
# for_perm(r)

print("product")
import itertools
print(list(itertools.product(nums, repeat=3)))

for i in range(6):
    if i not in nums:
        break
else:
    print("else")