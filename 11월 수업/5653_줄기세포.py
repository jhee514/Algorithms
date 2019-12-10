import sys
sys.stdin = open("5653_input.txt", "r")


T = int(input())
for _ in range(T):
    n, m, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    for g in range(n):
        print(grid[g])

    dead = [[0]*m for _ in range(n)]

    t = 0
    while t < k:
        t += 1
        for i in range(n):
