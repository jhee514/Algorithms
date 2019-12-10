import sys
sys.stdin = open("input_4880.txt", "r")


def compare(arr):
    a, b = arr[0], arr[1]
    if a[1] == 1 and b[1] == 3:
        return a
    elif a[1] == 3 and b[1] == 1:
        return b
    else:
        if a[1] == b[1]:
            if a[0] < b[0]:
                return a
            else:
                return b
        if a[1] > b[1]:
            return a
        if a[1] < b[1]:
            return b

def find(arr):
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return compare(arr)
    if len(arr) > 2:
        c = find(arr[:(1+len(arr))//2])
        d = find(arr[(1+len(arr))//2:])
        return find([c, d])


T = int(input())
for t in range(T):
    n = int(input())
    cards = list(map(int, input().split()))
    arr = [[0]* 2 for _ in range(n)]
    for i in range(n):
        arr[i][0] = i + 1
        arr[i][1] = cards[i]
    print("#{} {}".format(t+1, find(arr)[0]))