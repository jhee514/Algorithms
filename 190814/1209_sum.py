import sys
sys.stdin = open("solve_input.txt", "r")

for tc in range(10):
    tc = int(input())
    arr = [[0 for a in range(100)] for a in range(100)]
    for i in range(100):
        arr[i] = list(map(int, input().split()))
    sum = []
    for x in range(100):
        total = 0
        for y in range(100):
            total += arr[x][y]
        sum.append(total)
    for y in range(100):
        total = 0
        for x in range(100):
            total += arr[x][y]
        sum.append(total)
    for n in range(100):
        total = 0
        total += arr[n][n]
    sum.append(total)
    for s in range(len(sum)-1):
        min = s
        for j in range(s+1, len(sum)):
            if sum[min] > sum[j]:
                min = j
        sum[s], sum[min] = sum[min], sum[s]
    print("#%d %d" % (tc, sum[-1]))


# sol.
# for tc in range(10):
#     tc = int(input())
#     matrix = [list(map(int, input().split())) for _ in range(100)]

maxsum = sum = 0
