import sys

sys.stdin = open("input_1206.txt", "r")

def find(N, H):
    count = 0
    for i in range(2, N-2):
        sur = [H[i-2], H[i-1], H[i+1], H[i+2]]
        if max(sur) < H[i]:
            count += H[i] - max(sur)
    return count

T = 10  # T = int(input())
for tc in range(1, T+1):
    N = int(input())
    H = list(map(int, input().split()))


    res = find(N, H)
    print("#%d %d" % (tc, res))
