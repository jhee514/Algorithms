import sys
sys.stdin = open("4012_input.txt", "r")



"""
n개의 인덱스
    => N/2 개 의 조합

[1, 2, 3]

각각의 시너지 값
for i in comb:
    for j in comb:
        syn += data[i][j]

차이값
"""
import itertools

def synergy(comb):
    total = 0
    for i in comb:
        for j in comb:
            total += data[i][j]
    return total


T = int(input())
for tc in range(T):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]

    min_diff = 1000000

    food = list(range(n))
    combis = list(itertools.combinations(food, n//2))
    l = len(combis)
    for i in range(l//2):
        syn_1 = synergy(combis[i])
        syn_2 = synergy(combis[l-1-i])
        if abs(syn_1-syn_2) < min_diff:
            min_diff = abs(syn_1-syn_2)

    print("#{} {}".format(tc+1, min_diff))

