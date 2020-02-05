import sys
sys.stdin = open("input_15649.txt", "r")

def perm(k, R):
    if k == R :
        result = []
        for kk in range(k):
            result.append(str(t[kk]))
        print(' '.join(result))
    else:
        for i in range(n):
            t[k] = i + 1
            perm(k + 1, R)

n, m = map(int, input().split())
t = [0] * m
perm(0, m)