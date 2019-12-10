import sys

sys.stdin = open("input_5204.txt", "r")


def merge(left, right):
    global cnt
    result = []
    i, j = 0, 0
    if left[-1] > right[-1]:
        cnt += 1

    while len(left) > i and len(right) > j:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def merge_sort(m):
    if len(m) <= 1:
        return m
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


T = int(input())
for tc in range(T):
    n = int(input())
    data = list(map(int, input().split()))
    cnt = 0
    sorted = merge_sort(data)
    print("#{} {} {}".format(tc + 1, sorted[n // 2], cnt))
