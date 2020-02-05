n = int(input())
six = [0]*10000
m = 666
cnt = 0
while cnt < n:
    if '666' in str(m):
        six[cnt] = m
        cnt += 1
    m += 1
print(six[n-1])

