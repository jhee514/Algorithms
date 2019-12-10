import sys

sys.stdin = open("sample_input_5205.txt", "r")
import time

start = time.time()


def Hoare_partition(data, l, r):
    p = data[l]
    i = l
    j = r
    while i < j:
        while i < r and data[i] <= p:
            i += 1
        while j > l and data[j] > p:
            j -= 1
        if i < j:
            data[i], data[j] = data[j], data[i]
    data[l], data[j] = data[j], data[l]
    return j


def hoare_quick(data, l, r):
    if l < r:
        s = Hoare_partition(data, l, r)
        # hoare_quick(data, l, s - 1)
        """
        이렇게 하면 n//2 뒷 부분은 정렬이 필요가 없으니까 이렇게 설정해주면 부분 정렬이 된다 
        """
        if s < (n//2):
            hoare_quick(data, s + 1, r)


T = int(input())
for tc in range(T):
    n = int(input())
    data = list(map(int, input().split()))
    hoare_quick(data, 0, n - 1)
    print("#{} {}".format(tc + 1, data[n // 2]))

    print("time :", time.time() - start)
