import sys

sys.stdin = open("input_5207.txt", "r")

T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    a_list.sort()
    b_list = list(map(int, input().split()))

    cnt = 0
    for b in b_list:
        left = 0
        right = n - 1
        dir = 0
        # 0 base, 1 left, 2 right
        while left <= right:
            mid = (right + left) // 2
            if a_list[mid] == b:
                cnt += 1
                break
            elif a_list[mid] > b:
                if dir != 1:
                    dir = 1
                    right = mid - 1
                else:
                    break
            else:
                if dir != 2:
                    dir = 2
                    left = mid + 1
                else:
                    break
    print("#{} {}".format(tc + 1, cnt))
