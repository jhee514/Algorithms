import sys
sys.stdin = open("input.txt", "r")

sys.setrecursionlimit(10**8)

import time
start = time.time()
print("time :", time.time() - start)

T = int(input())
for tc in range(T):
    k, n, m = map(int, input().split())
    l = list(map(int, input().split()))
    data = [list(map(int, input())) for _ in range(n)]
    matrix = [list(map(int, input().split())) for _ in range(n)]
    table = [list(input()) for _ in range(n)]
    print("#{} {}".format(tc+1, ??))
