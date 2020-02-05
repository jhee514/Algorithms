import sys
sys.stdin = open("1952_input.txt", "r")

"""
각 달이 가질 수 있는 경우의 수는 4가지 일 월 삼 년
년으로 끊는 경우의 수는 단 하나
나머지는 일, 월, 삼 인데
해당 삼개월로 끊으면 나머지 두달은 자동으로 0원
"""

def comb(cnt = 0, cost = 0):
    global min_cost
    if cnt == 12:
        if cost < min_cost:
            min_cost = cost
    else:
        if cost < min_cost:
            comb(cnt+3, cost + quarterly)
            if swim[cnt] != 0:
                comb(cnt+1, cost + swim[cnt]*daily)
                comb(cnt+1, cost + monthly)
            else:
                comb(cnt + 1, cost)


T = int(input())
for tc in range(T):
    daily, monthly, quarterly, annual = map(int, input().split())
    swim = list(map(int, input().split()))
    min_cost = daily * 365
    if min_cost > annual:
        min_cost = annual
    comb()
    print("#{} {}".format(tc+1, min_cost))
