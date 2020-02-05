import sys

sys.stdin = open("input_1992.txt", "r")


def is_valid(arr, n):
    for i in range(n):
        for j in range(n):
            if arr[i][j] != arr[0][0]:
                return False
    else:
        return True


def split(arr, n):
    arr_1 = [[0] * (n // 2) for _ in range(n // 2)]
    arr_2 = [[0] * (n // 2) for _ in range(n // 2)]
    arr_3 = [[0] * (n // 2) for _ in range(n // 2)]
    arr_4 = [[0] * (n // 2) for _ in range(n // 2)]
    for i in range(n):
        for j in range(n):
            if i < n // 2 and j < n // 2:
                arr_1[i][j] = arr[i][j]
            elif n // 2 <= j and i < n // 2:
                arr_2[i][j - n // 2] = arr[i][j]
            elif n // 2 <= i and j < n // 2:
                arr_3[i - n // 2][j] = arr[i][j]
            else:
                arr_4[i - n // 2][j - n // 2] = arr[i][j]
    splitted = [arr_1, arr_2, arr_3, arr_4]
    return splitted


def paper(arr, n):
    global result
    if is_valid(arr, n):
        result += str(arr[0][0])
    else:
        splitted = split(arr, n)
        result += '('
        paper(splitted[0], n // 2)
        paper(splitted[1], n // 2)
        paper(splitted[2], n // 2)
        paper(splitted[3], n // 2)
        result += ')'


def find(data, n):
    global result
    if is_valid(data, n):
        if data[0][0] == 0:
            print(0)
            return
        else:
            print(1)
            return
    else:
        paper(data, n)
        print(result)
        return


n = int(input())
data = [list(map(int, input())) for _ in range(n)]
result = ''
find(data, n)

for _ in range(7):
    n = int(input())
    data = [list(map(int, input())) for _ in range(n)]
    result = ''
    find(data, n)
