import sys
sys.stdin = open("4008_input.txt", "r")


##################################################################
# 시간초과

def calculator(ops, k):
    result = data[0]
    kk = 0
    while kk < k:
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
        kk += 1
    return result


def ops_perm(k):
    global min, max
    if k == l:
        result = calculator(ops, k)

        if result > max:
            max = result
        if result < min:
            min = result
    else:
        for i in range(k, l):
            ops[i], ops[k] = ops[k], ops[i]
            ops_perm(k+1)
            ops[i], ops[k] = ops[k], ops[i]

T = int(input())
for tc in range(T):
    n = int(input())
    op = list(map(int, input().split()))
    data = list(map(int, input().split()))
    ops = []
    for o in range(4):
        for oo in range(op[o]):
            ops.append(o)
    l = len(ops)
    min, max = 10 ** 10, 10 ** (10) * (-1)
    ops_perm(0)
    print("#{} {}".format(tc+1, max - min))

##################################################################


def calculator(n, a, b):
    global result
    if n == 0:
        # result = a + b
        return a + b
    if n == 1:
        # result = a - b
        return a - b
    if n == 2:
        # result = a * b
        return a * b
    if n == 3:
        if a < 0:
            return (abs(a) //b) * (-1)
        else:
            return a // b


def ops_perm(result, k=0):
    global min, max
    if k == l:
        if result > max:
            max = result
        if result < min:
            min = result
    else:
        for i in range(4):
            if op[i]:
                op[i] -= 1
                ops_perm(calculator(i, result, data[k + 1]), k+1)
                op[i] += 1


T = int(input())
for tc in range(T):
    n = int(input())
    op = list(map(int, input().split()))
    data = list(map(int, input().split()))
    l = sum(op)
    min, max = 10 ** 10, 10 ** (10) * (-1)
    result = data[0]
    ops_perm(data[0])
    print("#{} {}".format(tc+1, max - min))