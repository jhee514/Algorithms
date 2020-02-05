import sys

sys.stdin = open("input_5186.txt", "r")

def find(data):
    result = ''
    i = 0
    while data:
        i += 1
        if i > 13:
            return "overflow"
        else:
            result += str(int(data // (2 ** (-i))))
            if not data // (2 ** (-i)):
                continue
            else:
                data = data - 2 ** (-i)
    return result

T= int(input())
for tc in range(T):
    data = float(input())
    print("#{} {}".format(tc +1, find(data)))