n, k = map(int, input().split())
data = list(int(input()) for _ in range(n))
cnt = 0
for d in range(n - 1, -1, -1):
    if k // data[d]:
        cnt += (k // data[d])
        k -= (k // data[d]) * data[d]
print(cnt)
