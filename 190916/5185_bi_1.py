import sys

sys.stdin = open("input_5185.txt", "r")


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


T = int(input())
for tc in range(T):
    n, data = input().split()
    print("#{} {}".format(tc + 1, hex_bi(data)))
