import sys

sys.stdin = open("input_5097.txt", "r")


def find():
    for i in range(m):
        curr = data.pop(0)
        data.append(curr)
    return data[0]


T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    print("#{} {}".format(t + 1, find()))
