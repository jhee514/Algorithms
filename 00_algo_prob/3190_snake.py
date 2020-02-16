import sys
sys.stdin = open("3190_input.txt", "r")

for tc in range(3):
    n = int(input())
    k = int(input())
    apples = [list(map(int, input().split())) for _ in range(k)]
    l = int(input())
    dir = [list(input().split()) for _ in range(l)]


    data = [[0]*n for _ in range(n)]
    for apple in apples:
        data[apple[0]][apple[1]] = 1

    start = [0, 0]


"""
dir 앞에 있는 숫자 만큼 지나면 방향을 전환
엘 => 왼쪽으로 90도 회전
    좌 => 위 => 오 => 아래
디 => 오른쪽으로 90도 회전
    동 => 아래 => 왼쪽 => 위
"""

