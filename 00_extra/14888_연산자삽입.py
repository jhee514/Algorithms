import sys
sys.stdin = open("input_14888.txt", "r")

import time
start = time.time()

"""
nums의 perm 함수를 만들고
다 만들어진 수열 단계에서 op의 perm 을 실행
"""
"""
def nums_perm(k):
    if k == n:
        ops_perm(0, nums)
    else:
        for i in range(k, n):
            nums[i], nums[k] = nums[k], nums[i]
            nums_perm(k+1)
            nums[i], nums[k] = nums[k], nums[i]
"""

def ops_perm(k):
    global min, max
    if k == l:
        result = data[0]
        for kk in range(k):
            if ops[kk] == 0:
                result += data[kk + 1]
            elif ops[kk] == 1:
                result -= data[kk + 1]
            elif ops[kk] == 2:
                result *= data[kk + 1]
            elif ops[kk] == 3:
                if result < 0:
                    result = (abs(result) // data[kk + 1]) * (-1)
                else:
                    result //= data[kk + 1]
        if result > max:
            max = result
        if result < min:
            min = result
    else:
        for i in range(k, l):
            ops[i], ops[k] = ops[k], ops[i]
            ops_perm(k+1)
            ops[i], ops[k] = ops[k], ops[i]

n = int(input())
data = list(map(int, input().split()))
op = list(map(int, input().split()))
ops = []
for o in range(4):
    for oo in range(op[o]):
        ops.append(o)
l = len(ops)
min, max = 10 ** 10, 10 ** (10) * (-1)
ops_perm(0)
print(max)
print(min)

print("time :", time.time() - start)