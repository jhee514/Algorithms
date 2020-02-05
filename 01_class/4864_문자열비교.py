import sys
sys.stdin = open("input_4864.txt", "r")

T = int(input())
for tc in range(T):
    p = input()
    t = input()
    M = len(p)
    N = len(t)

    i = 0
    j = 0
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1

    if j == M:
        result = 1
    else:
        result = 0
    print("#%d %d" % (tc+1, result))