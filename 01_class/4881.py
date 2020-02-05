import sys
sys.stdin = open("input_4881.txt", "r")

def perm_i():
    for i1 in range(1, n+1):
        for i2 in range(1, n+1):
            if i2 != i1:
                print(i1, i2)


def perm_r(k):

    if k == n:
        print(t)
    else:
        for i in range(n):
            if visited[i]:
                continue
            t[k] = i
            visited[i] = 1
            perm_r(k + 1)



T = int(input())
for t in range(T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    t = [0] * n
    print(n, arr)
    print("#%d %d" % (t+1, perm_r(0)))