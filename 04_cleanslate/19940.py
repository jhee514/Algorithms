import sys
sys.stdin = open("19940_input.txt", "r")

"""
 20 30 40 50  
 6-4 6-3 6-2 6-1
 2   3    4   5
"""
def solution(t):
    cnt = [0] * 5
    if t == 100:
        cnt[0] += 1
        cnt[1] += 1
        return cnt

    a = t // 10
    b = t % 10

    if a > 5:
        cnt[0] += 1
        cnt[1] += (a-6)

    elif 3 < a:
        cnt[0] += 1
        cnt[2] += (6-a)

    else:
        cnt[1] += a

    if b > 5:
        cnt[1] += 1
        cnt[4] += (10-b)
    else:
        cnt[3] += b
    return cnt


for _ in range(int(input())):
    data = int(input())
    ans = solution(data)
    print(' '.join(str(a) for a in ans))