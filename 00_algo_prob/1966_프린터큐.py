"""
확인하고 싶은 대상의 우선순위보다 큰 애가 있으면 그 애부터 그 뒤로 내 우선순위와 같거나 큰 애들의 갯수를 수해
"""
from collections import deque
import sys
sys.stdin = open("input_1966.txt", "r")

T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    prior = list(map(int, input().split()))
    target = prior[m]
    bigger = m
    for i in range(m, n):
        if prior[i] > target:
            bigger = i
            break
    cnt = 1
    if bigger > m:
        for ii in range(bigger, n):
            if prior[ii] >= target:
                cnt += 1
    for iii in range(m):
        if prior[iii] > target:
            cnt += 1
    print(cnt)