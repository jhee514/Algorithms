# 전자 기출 이라는 썰...
"""
인풋에서 8개 번호 세트를 추출해서 is_valid() 에 돌려서 valid 한 암호인지 검사하고
유효한 암호이면 암호의 개별 숫자들을 더한 add_nums() 에 돌려서 result 를 얻어
"""
import sys

sys.stdin = open("input_1240.txt", "r")


def is_valid(num_list):
    odds = 0
    result = 0
    for i in range(8):
        if i == 7:
            result += num_list[i]
        elif i % 2 == 0:
            odds += num_list[i]
        elif i % 2:
            result += num_list[i]
    result += odds * 3
    if result % 10 == 0:
        return True
    else:
        return False


def add_nums(nums):
    result = 0
    for n in nums:
        result += n
    return result


def find():
    result = [0] * 8
    for i in range(n):
        for j in range(m - 1, 54, -1):
            if data[i][j] == '1':
                cur = j
                cnt = 8
                while cnt:
                    cnt -= 1
                    if data[i][cur - 6:cur + 1] in code.keys():
                        result[cnt] = code[data[i][cur - 6:cur + 1]]
                    else:
                        break
                    cur -= 7
                if is_valid(result):
                    return result
    return False


T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    data = [str(input()) for _ in range(n)]
    # code = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111',
    # '0001011']
    code = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6,
            '0111011': 7, '0110111': 8,
            '0001011': 9}

    result = find()
    if find():
        out = add_nums(result)
    else:
        out = 0
    print("#{} {}".format(tc + 1, out))