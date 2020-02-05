import sys
sys.stdin = open("input_palin1.txt", "r")

def find(n, table):
    cnt = 0
    for i in range(8):
        for j in range(8-n+1):
            p = table[i][j:j+n]
            if p == p[::-1]:
                cnt += 1
    for k in range(8):
        for l in range(8-n+1):
            p = [table[m][k] for m in range(l, l+n)]
            if p == p[::-1]:
                cnt += 1
    return cnt

for tc in range(10):
    n = int(input())
    table = [list(input()) for _ in range(8)]
    print("#%d %d" % (tc+1, find(n, table)))


# sol.
# TODO : i, j index만 잘 바꿔줘도 시간이 훨씬 줄어들 것 => how??

def find(n, table):
    cnt = 0
    for i in range(8):
        for j in range(8-n+1):
            p = table[i][j:j+n]
            if p == p[::-1]:
                cnt += 1
    for k in range(8):
        for l in range(8-n+1):
            p = [table[m][k] for m in range(l, l+n)]
            if p == p[::-1]:
                cnt += 1
    return cnt