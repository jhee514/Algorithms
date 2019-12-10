import sys

sys.stdin = open("14890_input.txt", 'r')
"""
완전탐색 => 모든 row, col 검사

blocked = [0] * n
nums = [1, 1, ...] 리스트 안에 각각의 row 및 col 값을 넣

nums[i] - nums[i+1] 차이가 1 이상 일 때 => break
nums[i] - nums[i+1] 차이가 -1일 때,
    i-l+1 부터 i 번째 까지 같은 높이 + not blocked 일 때
        i-l+! 부터 i 번째 까지 blocked 처리 + continue
    else:
        break

nums[i] - nums[i+1] 차이가 +1일 때,
    i+1 부터 i+l 까지 숫자가 같으면 continue
        그럼 숫자가 작은 쪽을 i+1 부터 i+l 까지 blocked 처리
    else 면 break
"""


def is_path(i, nums, blocked, cnt=0, ):
    global right_path
    if i+1 == n:
        right_path += 1
        return
    elif nums[i] - nums[i + 1] > 1 or nums[i + 1] - nums[i] > 1:
        return False
    elif nums[i] == nums[i+1]:
        # TODO; if blocked 이면 cnt 가 안되어야한다 / 또한 지나가면 cnt 는 리셋이 되어야 한다
        if cnt == 0:
            if blocked[i]:
                is_path(i + 1, nums, blocked, cnt + 1)
            else:
                is_path(i + 1, nums, blocked, cnt + 2)
        else:
            if blocked[i]:
                is_path(i + 1, nums, blocked, cnt)
            else:
                is_path(i + 1, nums, blocked, cnt + 1)
    elif nums[i] - nums[i + 1] == 1:
        if i + l < n:
            for ii in range(i + 1, i + l):
                if nums[ii] != nums[ii + 1]:
                    return False
            for iii in range(i + 1, i + 1 + l):
                if blocked[iii]:
                    return False
                else:
                    blocked[iii] = 1
            is_path(i + l, nums, blocked)
    elif nums[i] - nums[i+1] == -1:
        if cnt >= l:
            is_path(i + 1, nums, blocked)
        else:
            return


# n, l = 6, 2
# right_path = 0
# blocked = [0] * n
# nums = [3, 2, 2, 2, 3, 3]
# is_path(0, nums, blocked)
# print(right_path)


for tc in range(4):
    n, l = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]

    right_path = 0
    for i in range(n):
        blocked = [0]*n
        is_path(0, data[i], blocked)
        blocked = [0]*n
        nums = [0] * n
        for j in range(n):
            nums[j] = data[j][i]
        is_path(0, nums, blocked)
    print(right_path)
