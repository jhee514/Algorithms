n, k = map(int, input().split())
q = list(range(1, n + 1))
result = []
temp = 0
while len(q) > 1:
    while temp + k - 1 > len(q) - 1:
        temp -= len(q)
    result.append(q.pop(temp + k - 1))
    temp += k - 1
print("<", end='')
for i in result:
    print(i, end="")
    print(", ", end='')
print(q[-1], end='')
print(">")
