import sys
from collections import deque

sys.stdin = open("input_5108.txt", "r")


def find():
    q = deque(nums)
    for i in range(m):
        q.insert(to_append[i][0], to_append[i][1])
    return q[l]


T = int(input())
for tc in range(T):
    n, m, l = map(int, input().split())
    nums = list(map(int, input().split()))
    to_append = [list(map(int, input().split())) for _ in range(m)]
    print("#{} {}".format(tc + 1, find()))
