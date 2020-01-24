import sys

sys.stdin = open("2529_input.txt", "r")

"""
10개의 숫자 중에서 k 개를 순열로 가져와
부등호를 사이사이 넣어봐
중간에 가지치기 해주면서 쭉 돌아야

"""

import itertools


def sol(k, data):
    nums = list(range(10))
    min_num, max_num = 10 ** (k + 1), 0
    perms = itertools.permutations(nums, k + 1)
    for p in perms:
        if p == (1, 0, 2, 3, 4, 5, 6, 7, 9, 8):
            a = 1
        for i in range(k):
            if data[i] == '>' and p[i] < p[i + 1]:
                break
            elif data[i] == '<' and p[i] > p[i + 1]:
                break
                # > < < < > > > < <
        else:
            str_num = ''
            for pp in p:
                str_num += str(pp)
            if int(str_num) < min_num:
                min_num = int(str_num)
                str_min = str_num
            if int(str_num) > max_num:
                max_num = int(str_num)
                str_max = max_num
    print(str_max)
    print(str_min)


T = 2
for tc in range(T):
    k = int(input())
    data = list(map(str, input().split()))
    sol(k, data)
