import sys

sys.stdin = open("input_2217.txt", "r")

n = int(input())
data = list(int(input()) for _ in range(n))
data.sort(reverse=True)
max = 0
for i in range(n):
    if data[i] * (i + 1) > max:
        max = data[i] * (i + 1)
print(max)
