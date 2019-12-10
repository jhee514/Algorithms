import sys
sys.stdin = open("input_ladder.txt", "r")

def safe(a, b):
    return 0 <= y < 100 and 0 <= x < 100 and data[a][b] == 1


def find(data):
    b = data[-1].index(2)

# TODO : stack 이 필요한 경우는 지나온 길을 알아야 좌우 갈림길을 갈 때 왔던 방향으로 가지 않도록 해주는 것?



    return b


for t in range(10):
    tc = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    print("#%d %d" % (tc, find(data)))