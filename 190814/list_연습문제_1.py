import math
import random

n = 5

l0 = [0] * (n+2)
l1 = [0] * (n+2)
l2 = [0] * (n+2)
l3 = [0] * (n+2)
l4 = [0] * (n+2)
l5 = [0] * (n+2)
l6 = [0] * (n+2)
arr = [l0, l1, l2, l3, l4, l5, l6]

# arr = [[0 for x in range(n+2)] for x in range(n+2)]


num_list = [num for num in range(1, n**2 + 1)]
shuf = random.sample(num_list, len(num_list))

for i in range(1, n+1):
    l1[i] = shuf.pop()
    l2[i] = shuf.pop()
    l3[i] = shuf.pop()
    l4[i] = shuf.pop()
    l5[i] = shuf.pop()

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

total = 0
for x in range(1, len(arr)-1):
    for y in range(1, len(arr[x])-1):
        for i in range(len(dx)):
            total += abs(arr[x][y] - arr[x+dx[i]][y+dy[i]])

# TODO : 가장자리 숫자들은 두번씩 더 더해지는 에러

print(total)


# sol.

arr = [[0 for x in range(n+2)] for x in range(n+2)]
for i in range(5):
    arr[i] = list(map(int, input().split()))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

sum = 0
for x in range(len(arr)):
    for y in range(len(arr[0])):
        for i in range(4):
            textX = x + dx[i]
            textY = y + dy[i]
            if isWall(testX, textY) == False:
                sum += calAbs(arr[x][y], arr[testX][textY])

print("sum = %d" %sum)