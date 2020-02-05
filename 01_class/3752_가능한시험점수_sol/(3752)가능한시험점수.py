#DP
import sys
sys.stdin = open("(3752)가능한시험점수_input.txt")
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    pt = [0 for _ in range(N+1)]
    temp = list(map(int, input().split()))
    sum = 0

    for i in range(N): #원소의 합 구하기 인덱스1부터 조정
        pt[i+1] = temp[i]
        sum += temp[i]

    memo = [[0 for _ in range(sum+1)] for _ in range(N+1)]

    for i in range(0, N+1):
        memo[i][0] = 1

    memo[1][pt[1]] = 1

    for i in range(2, N+1):
        for j in range(sum+1):
            if memo[i-1][j] :
                memo[i][j] = memo[i][j+pt[i]] = 1

    cnt = 0
    for i in range(sum+1):
        cnt += memo[N][i]

    print("#{} {}".format(tc, cnt))

