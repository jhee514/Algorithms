import sys
sys.stdin = open("input_sum.txt", "r")

# def max_sum(m, nums):
#     return max([sum(nums[i:i+m]) for i in range(len(nums)-m+1)]) - min([sum(nums[i:i+m]) for i in range(len(nums)-m+1)])

def block_sum(n, m, nums):
    maxTotal = sum(nums[:m])
    minTotal = sum(nums[:m])
    for i in range(1, n-m+1):
        if sum(nums[i:i+m]) > maxTotal:
            maxTotal = sum(nums[i:i+m])
        if sum(nums[i:i+m]) < minTotal:
            minTotal = sum(nums[i:i+m])
    return maxTotal - minTotal

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    print("#%d %d" % (tc, block_sum(n, m, nums)))


# sol.1
def find(n, m):
    maxV = 0
    minV = 10000000
    for i in range(0, n - m + 1):
        s = 0
        for j in range(i, i+m):
            s = s+ v[j]
        if s > maxV:
            maxV = s
        if s < minV:
            minV = s

# sol.2
def find(n, m):
    sum = 0
    for i in range(0, m):
        sum += v[i]
    minV = sum
    maxV = sum
    for i in range(1, n - m + 1):
        sum = sum - v[i - 1] + v[i + m + 1]
        if sum > maxV:
            maxV = sum
        if sum < minV
            minV = sum
    return maxV - minV