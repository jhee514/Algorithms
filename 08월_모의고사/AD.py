import sys

sys.stdin = open("sample_input_a.txt", 'r')


def check(nums):
    for i in range(len(nums) - 1):
        if abs(nums[i] - nums[i + 1]) > 1:
            return False
    else:
        return True


def find(data, cnt=0):
    if check(data):
        return cnt
    else:
        while cnt < 6:
            cnt += 1
            left = data[:n // 2]
            right = data[n // 2:]
            # for i in range(1, cnt):  # i 는 셔플 회수
            about_to = left[-cnt:] + right[:cnt]
            for j in range(len(about_to) // 2):
                about_to[j * 2], about_to[j * 2 + 1] = about_to[j * 2 + 1], about_to[j * 2]
            shuffled = left[:-cnt] + about_to + right[cnt:]
            return find(shuffled, cnt)

        else:
            return -1


T = int(input())
for t in range(T):
    n = int(input())
    cards = list(map(int, input().split()))
    print("#%d %d" % (t + 1, find(cards)))
