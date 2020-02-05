import sys
sys.stdin = open("(3752)가능한시험점수_input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    pt = list(map(int, input().split()))
    # temp = 0
    # # ans = 0
    # for i in range(N):
    #     temp += pt[i] #원소의 합

    #score = [0 for _ in range(temp+1)]
    score = set()

    for i in range(1 << N):
        sum = 0
        for j in range(N+1):
            if i & (1 << j):
                sum += pt[j]
            #score[sum] = 1
            score.update([sum])

    print("#{} {}".format(tc, len(score)))
    # for i in range(temp+1):
    #     if score[i]: ans += 1
    #
    # print("#{} {}".format(tc, ans))