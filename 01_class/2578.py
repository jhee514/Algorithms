import sys
sys.stdin = open("input_2578.txt", "r")

data = [list(map(int, input().split())) for _ in range(10)]
bingo = data[:5]
numbers = [j for i in range(5, 10) for j in data[i]]

def check(bingo):
    cnt = 0
    row1 = [1] * 5
    row2 = [1] * 5
    for z in range(5):
        if bingo[z] == [0] * 5:
            cnt += 1

        row1[z] = bingo[z][z]
        row2[z] = bingo[4-z][z]

        row3 = [1] * 5
        for y in range(5):
            row3[y] = bingo[y][z]
        if row3 == [0] * 5:
            cnt += 1
    if row1 == [0] * 5:
        cnt += 1
    if row2 == [0] * 5:
        cnt += 1
    return cnt

def find(bingo, numbers):
    for k in numbers:
        for l in range(5):
            for m in range(5):
                if bingo[l][m] == k:
                    bingo[l][m] = 0
                    if check(bingo) < 3:
                        break
                    elif check(bingo) > 2:
                        print(numbers.index(k) + 1)
                        return

find(bingo, numbers)