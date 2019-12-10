import sys
sys.stdin = open("input_4869.txt", "r")

def find(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    if n in range(3, 31):
        return find(n-1) + 2 * find(n-2)

T = int(input())
for tc in range(T):
    n = int(input()) // 10
    print("#%d %d" % (tc+1, find(n)))