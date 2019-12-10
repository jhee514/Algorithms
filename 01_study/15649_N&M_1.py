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
            if visited[i]:
                continue
            t[k] = i + 1
            visited[i] = 1
            perm(k + 1, R)
            visited[i] = 0

for tc in range(3):
    n, m = map(int, input().split())
    visited = [0] * n
    t = [0] * m
    perm(0, m)