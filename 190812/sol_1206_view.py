T = 10  # T = int(input())
for tc in range(1, T+1):
    N = int(input())

    H = list(map(int, input().split()))


    res = find(N, H)
    print("#%d %d" % (tc, res))


def getmax():
    if H[i-2] > H[i]:
        hmax = H[i-2]
    if H[i-1] > [H]
        hmax = ...