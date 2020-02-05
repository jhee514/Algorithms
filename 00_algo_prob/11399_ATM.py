n = int(input())
data = list(map(int, input().split()))
data.sort()
total = 0
for i in range(n):
    total += sum(data[:i + 1])
print(total)

n = int(input())
data = list(map(int, input().split()))
data.sort()
total = 0
for i in range(n):
    for j in range(i + 1):
        total += data[j]
print(total)
