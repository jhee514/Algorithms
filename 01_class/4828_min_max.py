import sys
sys.stdin = open("input_min.txt", "r")

# def minmax(nums):
#     return max(nums) - min(nums)

# sol.
def fine(a, n):
    maxValue = a[0]
    minValue = a[0]
    for i in range(1, n):
        if a[i] > maxValue:
            maxValue = a[i]
        if a[i] < minValue:
            minValue = a[i]
    return maxValue - minValue

T = int(input())
for tc in range(1, T + 1):
    # l = int(input())
    # nums = list(map(int, input().split()))
    # print("#%d %d" % (tc, minmax(nums)))
    N = int(input())
    v = list(map(int, input().split()))
    print("#%d %d" % (tc, fine(v, N)))