import sys
sys.stdin = open("input_sort.txt", "r")

def sort(n, l):
    for i in range(0, n-1):
        min = i
        for j in range(i+1, n):
            if l[min] > l[j]:
                min = j
        l[i], l[min] = l[min], l[i]

    sorted = [0 for _ in range(10)]
    for k in range(5):
        sorted[k*2] = l[-1-k]
        sorted[k*2+1] = l[k]
    return ' '.join([str(n) for n in sorted])

T = int(input())
for t in range(T):
    n= int(input())
    l = list(map(int, input().split()))
    print("#%d %s" % (t+1, sort(n, l)))