import sys
sys.stdin = open("input_metal.txt", "r")

T = int(input())
for tc in range(T):
    n = int(input())
    arr = [[0 for _ in range(2)] for _ in range(n)]
    nails = list(map(int, input().split()))

    i = 0
    for x in range(n):
        for y in range(2):
            arr[x][y] = nails[i]
            i += 1

    for j in range(n - 1):
        min = j
        for k in range(j + 1, n):
            if arr[min][0] > arr[k][0]:
                min = k
        arr[j], arr[min] = arr[min], arr[j]


    print(arr)


# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     sizes = list(map(int, input().split()))
#
#     for i in range(len(sizes)):  # 맨앞자리 빼주기( 짝수 자리 중에 하나밖에 없는 것.)
#         if i % 2 == 0:
#             if sizes.count(sizes[i]) == 1:
#                 sizes[i], sizes[0] = sizes[0], sizes[i]
#                 sizes[i+1], sizes[1] = sizes[1], sizes[i+1]
#
#     for i in range(2, len(sizes)-1, 2):  # 2자리 씩 슬라이싱 주면서 같으면 자리 교환
#         for j in range(3, len(sizes), 2):
#             if sizes[j-1] == sizes[i-1]:
#                 sizes[i], sizes[j-1] = sizes[j-1], sizes[i]
#                 sizes[i+1], sizes[j] = sizes[j], sizes[i+1]
#
#     result = str(sizes)[1:-1].replace(',', '')
#
#     print('#{} {}'.format(tc, result))