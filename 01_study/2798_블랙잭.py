def comb(r, n, total=0):
    global max_sum
    if r == 0:
        if max_sum < total <= m:
            max_sum = total
    elif n < r:
        return
    else:
        if total + data[n-1] <= m:
            comb(r-1, n-1, total+data[n-1])
        comb(r, n-1, total)

n, m  = map(int, input().split())
data = list(map(int, input().split()))
max_sum = 0
comb(3, n)
print(max_sum)
