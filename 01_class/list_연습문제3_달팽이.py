array = [[9, 20, 2, 18, 11], [19, 1, 25, 3, 21], [8, 24, 10, 17, 7], [15, 4, 16, 5, 6], [12, 13, 22, 23, 14]]
nums = []

for x in range(len(array)):
    for y in range(len(array[0])):
        nums.append(array[x][y])

for n in range(len(nums) - 1):
    min = n
    for j in range(n + 1, len(nums)):
        if nums[min] > nums[j]:
            min = j
    nums[n], nums[min] = nums[min], nums[n]

arr = [[0 for a in range(5)] for a in range(5)]


n = 5
y = 0
for x in range(n):
    arr[x][y] =

print(arr)
