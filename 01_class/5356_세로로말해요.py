import sys

sys.stdin = open("input_5356.txt", "r")

def find():
    result = []
    for i in range(5):
        while len(letters[i]) != 15:
            letters[i].append(' ')
    for q in range(15):
        for p in range(5):
            if letters[p][q] != ' ':
                result.append(letters[p][q])
    return ''.join(result)

T = int(input())
for tc in range(T):
    letters = [list(input()) for _ in range(5)]
    print("#{} {}".format(tc + 1, find()))
