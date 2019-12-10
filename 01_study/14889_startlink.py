import sys
sys.stdin = open("input_14889.txt", "r")
"""
조합 n//2 개
나머지 n//2 개
각각에 for i
        for j 
토탈에 저장
"""

def comb(r, n):
    global min_dif
    if r == 0:
        dif = 0
        link = [0] * (total//2)
        no = 0
        for i in arr:
            if i not in start:
                link[no] = i
                no += 1
        for ii in range(total // 2 -1):
            for jj in range(ii+1, total // 2):
                dif += data[start[ii]][start[jj]]
                dif += data[start[jj]][start[ii]]
                dif -= data[link[ii]][link[jj]]
                dif -= data[link[jj]][link[ii]]
        if abs(dif) < min_dif:
            min_dif = abs(dif)
        return
    elif n < r:
        return
    else:
        start[r-1] = arr[n-1]
        comb(r-1, n-1)
        comb(r, n-1)


for tc in range(3):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    arr = list(range(n))
    start = [0] * (n // 2)
    min_dif = 100*20
    total = n
    comb(n // 2, n)
    print(min_dif)