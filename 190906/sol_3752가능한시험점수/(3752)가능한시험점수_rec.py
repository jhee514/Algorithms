import sys
sys.stdin = open("(3752)가능한시험점수_input.txt")

def powerset(n, k, sum):
    if n == k:
        score[sum] = 1
    else:
        A[k] = 1
        powerset(n, k+1, sum+pt[k])
        A[k] = 0
        powerset(n, k+1, sum)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    pt = list(map(int, input().split()))
    A =[0 for _ in range(N)]

    temp = 0
    for i in range(N):
        temp += pt[i]  # 원소의 합
    score = [0 for _ in range(temp + 1)]

    powerset(N, 0, 0)

    ans = 0
    for i in range(temp+1):
        if score[i]: ans += 1

    print("#{} {}".format(tc, ans))