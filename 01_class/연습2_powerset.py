def comb(n, r, arr, total=0):
    if r == 0:
        if total == 10:
            print(temp, end=' ')
    elif n < r:
        return
    else:
        temp[r - 1] = arr[n - 1]
        if total + temp[r - 1] < 10:
            comb(n - 1, r - 1, data, total + temp[r - 1])
        comb(n - 1, r, data, total)


def powersetlist(s):
    r = [[]]
    for e in s:
        temp = [x + [e] for x in r]
        r += temp
    return r


data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(data)

print("sum == 10")
for r in range(n + 1):
    temp = [0] * r
    comb(n, r, data)

print()

powerset = powersetlist(data)
for pp in powerset:
    if sum(pp) == 10:
        print(pp, end=' ')
