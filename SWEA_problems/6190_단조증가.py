import sys

sys.stdin = open("input_6190.txt", "r")


# 일단 다 곱한 조합을 모아
# 그 조합에서 단조증가 수를 모아
# 단조 증가 검사 법
# => % 10 값이 0 이 아닐 때까지 돌려서 그 몫들을 비교
# 거기서 맥스 값 출력
def ismono(n):
    right_digit = n % 10
    while n // 10 != 0:
        n = n // 10
        left_digit = n % 10
        if left_digit > right_digit:
            return False
        else:
            right_digit = left_digit
    return True

def find():
    mult = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            mult.append(nums[i] * nums[j])
    mono_inc = []
    for k in mult:
        if ismono(k):
            mono_inc.append(k)
    if mono_inc:
        return max(mono_inc)
    else:
        return -1


T = int(input())
for tc in range(T):
    n = int(input())
    nums = list(map(int, input().split()))
    print("#{} {}".format(tc + 1, find()))

# TODO Review
# 1.max 값을 하나 잡고 곱한 값이 이것 보다 작으면 애초에 비교 하지 않기
# 2.단조증가 볼 때 str 으로 가져와서 비교하면 훨씬 빠록
# 3.밖에 만든 함수 돌리는 것 보다 함수 하나에 연산 다 넣으면 더 빨라
