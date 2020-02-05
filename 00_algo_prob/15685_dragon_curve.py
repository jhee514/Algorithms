import sys
sys.stdin = open("15685_input.txt", "r")


for _ in range(4):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]


    print(data)