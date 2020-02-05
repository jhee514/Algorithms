import sys

sys.stdin = open("1120_input.txt", "r")
# output 2

"""
a 의 앞 또는 뒤 에 마무 알파벳이나 추가해서
a, b 의 길이가 같아졌을 때 cnt 가 최소 여야

몇개 차이인지 먼저 구하고
갯수 만큼 연산을 해주고 차이를 구해야
새로 추가된 문자는 무조건 b와 같은 문자라고 생각해야
앞에 추가하면 앞에 추가한 개수 뺀 범위(range(2, len(b)) 로 비교하고
뒤에 추가할 때도 같다.
"""


def sol(data):
    a, b = data.split()
    diff = len(b) - len(a)
    min_cnt = len(b)
    for d in range(diff + 1):
        cnt = 0
        for i in range(len(a)):
            if b[i + d] != a[i]:
                cnt += 1
        if cnt < min_cnt:
            min_cnt = cnt
    print(min_cnt)


T = int(input())
for tc in range(T):
    data = input()
    sol(data)
