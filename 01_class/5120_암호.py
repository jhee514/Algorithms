import sys

sys.stdin = open("input_5120.txt", "r")
from collections import deque


def find():
    q = deque(nums)
    curr = 0
    for _ in range(k):
        if curr + m < len(q):
            curr = curr + m
            q.insert(curr, q[curr - 1] + q[curr])

        elif curr + m == len(q):
            curr = curr + m
            q.append(q[-1] + q[0])
        else:
            curr = curr + m - len(q)
            q.insert(curr, q[curr - 1] + q[curr])
    result = []
    if len(q) > 10:
        for i in range(10):
            result.append(q[-1 - i])
    else:
        for i in range(len(q)):
            result.append(q[-1 - i])
    return ' '.join(map(str, result))


T = int(input())
for tc in range(T):
    n, m, k = map(int, input().split())
    nums = list(map(int, input().split()))
    print("#{} {}".format(tc + 1, find()))
