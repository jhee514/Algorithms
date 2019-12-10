import sys

sys.stdin = open("input_1242.txt", "r")

"""
16진수 => 2진수 => 몇배수로 들어오는지 체크 => 1배수 수로 전환 => 10진수 => is_valid => add
TODO : 일단 암호가 여러개 들어올 수 있고, 하나의 암호가 몇 배수로 쓰였는지 몰
"""
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
    for i in nums:
        result += i
    return result


def hex_bi(data):
    bi = {}
    for i in range(16):
        num = i
        temp = ''
        for j in range(3, -1, -1):
            temp += str(int(num) // (2 ** j))
            if int(num) // (2 ** j):
                num -= 2 ** j
        bi[i] = temp
    converted = ''
    for d in data:
        if d.isdigit():
            converted += bi[int(d)]
        else:
            converted += bi[ord(d) - ord("A") + 10]
    return converted

# def find(data):
#     mm = len(data) // 8 // 7  # code 가 몇 배수로 들어갔는지
#     result = [0] * 8
#     nn = len(data)
#     for j in range(nn - 1, 54, -1):
#         if data[j] == '1':
#             cur = j
#             cnt = 8
#             while cnt:
#                 cnt -= 1
#                 if data[cur - 6:cur + 1] in codes.keys():
#                     result[cnt] = codes[data[cur - 6:cur + 1]]
#                 else:
#                     break
#                 cur -= 7
#     return result

# TODO 뒤에서부터 봐야하나,,,? => 16진수를 2진수로 바꾼 애 안에서 뒤에서 1부터 찾아야
# TODO 그두에서부터 배수로 끊어가면서 2진수 숫자 개수를 세야 => (8 + 1) * n 개씩 끊어서 앞에 8개가 1이 있는지 없는지

# TODO 16진수 수를 어케 찾
def search(data):
    result = []
    for i in range(n):
        start = 0
        for j in range(m):
            if j < start:
                continue
            elif data[i][j] != '0':
                start = j + 1
                while data[i][start:start+2] != '00':
                    start += 1
                result.append(data[i][j:start])
                print(result)
    set_result = set(result)
    return set_result

codes = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6,
        '0111011': 7, '0110111': 8, '0001011': 9}

data = '196EBC5A316C578'
result = hex_bi(data)
code = []

for r in result:



print(len(result), result)

# T = int(input())
# for tc in range(T):
#     n, m = map(int, (input().split()))
#     raw = [str(input()) for _ in range(n)]
#     data = search(raw)
#     # TODO 왜 tc 가 2번까지 밖에 안나와!?
#     print("#{} {}".format(tc+1, data))
#

