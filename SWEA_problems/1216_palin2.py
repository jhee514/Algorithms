import sys
sys.stdin = open("input_palin2.txt", "r")

def find(table):
    maxlen = 0
    for n in range(100):
        for i in range(100):
            for j in range(100 - n + 1):
                p = table[i][j:j + n]
                if p == p[::-1] and len(p) > maxlen:
                    maxlen = len(p)
                    break
    for q in range(maxlen, 100):
        for k in range(100):
            for l in range(100 - q + 1):
                p = [table[m][k] for m in range(l, l + q)]
                if p == p[::-1] and len(p) > maxlen:
                    maxlen = len(p)
                    break


# def find(table):
#     maxlen = 0
#     for n in range(100):
#         for i in range(100):
#             for j in range(100 - n + 1):
#                 p = table[i][j:j + n]
#                 if p == p[::-1] and len(p) > maxlen:
#                     maxlen = len(p)
#                     break
#     r = maxlen
#     for q in range(r + 1, 100):
#         for k in range(100):
#             for l in range(100 - q + 1):
#                 p = [table[m][k] for m in range(l, l + q)]
#                 if p == p[::-1] and len(p) > maxlen:
#                     maxlen = len(p)
#                     break


    return maxlen


for _ in range(10):
    tc = int(input())
    table = [list(input()) for _ in range(100)]
    print("#%d %d" % (tc, find(table)))

    