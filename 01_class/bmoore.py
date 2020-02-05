def computejump():
    >>>>>

def bmoore(tstr, pstr):
    n = len(tstr)
    m = len(pstr)
    jump = [m for _ in range(128)]
    computejump(pstr, jump)

    i = 1
    cnt = 0
    while i < (n - m + 1):
        j = m - 1
        k = i + m - 1
        cnt += 1

        while j > 0 and pstr[j] ==tstr[k]:
            j -= 1
            k -= 1
            cnt += 1

        if j == 0:
            print("%d times computations" % cnt, end=" ")
            return i