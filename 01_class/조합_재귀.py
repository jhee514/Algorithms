nums = list(range(5))
t = [0]* 5

def comb(k, s):
    if k == range:
        print(t)
    else:
        for i in range(k, n-r+k+1):
            t[k] = a[i]
            comb(k+1, i+1)
for k in range(5):
    comb(k, )