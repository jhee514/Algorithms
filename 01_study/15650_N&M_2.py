import sys
sys.stdin = open("input_15649.txt", "r")


def perm(k, R):
    if k == R :
        result = []
        for kk in range(k):
            result.append(str(arr[kk]))
        print(' '.join(result))
    else:
        for i in range(k, n):
            arr[i], arr[k] = arr[k], arr[i]
            if k == 0:
                perm(k + 1, R)
            elif k > 0:
                if arr[k-1] < arr[k]:
                    perm(k+1, R)
            arr[i], arr[k] = arr[k], arr[i]


for tc in range(3):
    n, m = map(int, input().split())
    arr = [i for i in range(1, n+1)]
    perm(0, m)