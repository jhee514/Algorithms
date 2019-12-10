import sys
sys.stdin = open("input_5247.txt", "r")

def isvalid(a):
    if 1<= a <= 1000000 and not visited[a]:
        return True

T = int(input())
for tc in range(T):
    n, m = map(int, input().split())

    front = -1
    rear = -1

    q = [0] * 1000000
    depth = [0] * 1000000
    visited = [0] * 1000001
    rear += 1
    q[rear] = n

    while front != rear:
        front += 1
        cur = q[front]
        cur_depth = depth[front]

        if isvalid(cur + 1):
            rear += 1
            q[rear] = cur + 1
            depth[rear] = cur_depth + 1
            visited[cur + 1] = 1
            if q[rear] == m:
                break

        if isvalid(cur -1):
            rear += 1
            q[rear] = cur - 1
            depth[rear] = cur_depth + 1
            visited[cur - 1] = 1
            if q[rear] == m:
                break

        if isvalid(cur *2):
            rear += 1
            q[rear] = cur * 2
            depth[rear] = cur_depth + 1
            visited[cur *2] = 1
            if q[rear] == m:
                break

        if isvalid(cur -10):
            rear += 1
            q[rear] = cur - 10
            depth[rear] = cur_depth + 1
            visited[cur -10] = 1
            if q[rear] == m:
                break

    print("#{} {}".format(tc + 1, depth[rear]))


###############################################
#
# T = int(input())
# for tc in range(T):
#     n, m = map(int, input().split())
#
#     front = -1
#     rear = -1
#
#     q = [0] * 1000000
#     depth = [0] * 1000000
#     rear += 1
#     q[rear] = n
#
#     while front != rear:
#
#         front += 1
#         cur = q[front]
#         if 1 <= cur <= 1000000:
#             cur_depth = depth[front]
#
#             rear += 1
#             q[rear] = cur + 1
#             depth[rear] = cur_depth + 1
#             if q[rear] == m:
#                 break
#
#             rear += 1
#             q[rear] = cur - 1
#             depth[rear] = cur_depth + 1
#             if q[rear] == m:
#                 break
#
#             rear += 1
#             q[rear] = cur * 2
#             depth[rear] = cur_depth + 1
#             if q[rear] == m:
#                 break
#
#             rear += 1
#             q[rear] = cur - 10
#             depth[rear] = cur_depth + 1
#             if q[rear] == m:
#                 break
#
#     print("#{} {}".format(tc + 1, depth[rear]))
