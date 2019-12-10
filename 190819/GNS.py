import sys
sys.stdin = open("input_GNS.txt", "r")


# T = int(input())
# for tc in range(T):
#     c, N = input().split()
#     t = list(input().split())
#     n = int(N)
#
#     strings = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
#     numbers = [i for i in range(10)]
#     ns = dict(zip(strings, numbers))
#
#     for i in range(n):
#         t[i] = ns.get(t[i])
#     for j in range(n-1):
#         min = j
#         for k in range(j+1, n):
#             if t[min] > t[k]:
#                 min = k
#         t[j], t[min] = t[min], t[j]
#     for l in range(n):
#         for k, v in ns.items():
#             if t[l] == v:
#                 t[l] = k
#     print(c, ' '.join(t))


# 인덱싱 => 인덱스 번호 대로 정렬
#     strings = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
#
#     for i in range(n-1):
#         min = i
#         for j in range(i+1, n):
#             if strings.index(t[min]) > strings.index(t[j]):
#                 min = j
#         t[i], t[min] = t[min], t[i]
#     print(c, ' '.join(t))


# T = int(input())
# for tc in range(T):
#     c, d = input().split()
#     n = int(d)
#     ps = list(input().split())
#
#     words = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
#     t = ' '.join(words)
#
#     for l in range(n):
#         p = ps[l]
#         M = len(p)
#         N = len(t)
#
#         i = 0
#         j = 0
#         while j < M and i < N:
#             if t[i] != p[j]:
#                 i = i - j
#                 j = -1
#             i = i + 1
#             j = j + 1
#         if j == M:
#             ps[l] = words.index(p)
#
#     ps.sort()
#
#     for k in range(n):
#         ps[k] = words[ps[k]]
#
#     print(c, ' '.join(ps))



# TODO : dict는 다른 언어는 없는게 많으니까 cnt = [0] * 10 으로 리스트를 생성해서 값을 저장해서 각각의 cnt 값만큼 반복 출력을 해주는 것이 빠를 것.
T = int(input())
for tc in range(T):
    c, d = input().split()
    n = int(d)
    ps = list(input().split())

    words = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    t = ' '.join(words)

    word_cnt = {}

    for l in range(n):
        p = ps[l]
        M = len(p)
        N = len(t)

        i = 0
        j = 0
        while j < M and i < N:
            if t[i] != p[j]:
                i = i - j
                j = -1
            i = i + 1
            j = j + 1
        if j == M:

    print(word_cnt)


# sol

for _ in range(T):
    tc, N = input().split()
    N = int(N)