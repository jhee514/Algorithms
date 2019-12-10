import sys

sys.stdin = open("input_1493.txt", "r")


# p star q
# p가 찍힌 좌표 x, y 와 q 가 찍힌 좌표 z, w 를 더해 => (x+z, y+w)
# 그리고 (x+z, y+w) 이 좌표에 찍힌 점의 값을 도출

# n 번째 리스트 첫번째 숫자 구하기
# 0 ~ n-1 번째 리스트 안 숫자들의 개수 + 1

# n 번째 리스트에 n 개씩 담겨져 있다.
# 좌표를 통해 값을 찾는 방법
# (a, b)
# a + b - 1 개가 들어 있는 리스트(idx => a+b-1-1) 의 a번째(idx => a-1)


# n번째 집합의 첫번째 숫자 찾기
def first_num(n):
    cnt = 0
    for i in range(n):
        cnt += i
    return cnt + 1


# num 의 좌표 찾기
# n - 1 번째 집합에 num 이 들어 있다
# first_num(n-1) 이 num 이 들어있는 n -1 번째 집합의 첫번쨰 요소
# num - first_num(n-1) + 1 한 것이 x 좌표
# y 좌표 = n - 1 + 1 - (num - first_num(n-1) + 1)
def points(num):
    n = 1
    while first_num(n) <= num:
        n += 1
    return [num - first_num(n - 1) + 1, n - (num - first_num(n - 1) + 1)]


# 좌표료 숫자 찾기
def num(a):
    n = a[0] + a[1] - 1
    return (first_num(n) + a[0] - 1)


def add(a, b):
    return [a[0] + b[0], a[1] + b[1]]


def star(p, q):
    a, b = points(p), points(q)
    c = add(a, b)
    return num(c)


T = int(input())
for tc in range(T):
    p, q = map(int, input().split())
    print("#{} {}".format(tc + 1, star(p, q)))