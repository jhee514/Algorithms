import sys

sys.stdin = open("input_5176.txt", "r")

# 노드 번호는 루트부터 1번
# 요소 값은 완전이진탐색 트리를 중회 순회로 (밑에서부터 1부터)
# 완전이진트리 => node.left = node*2, node.right = node*2 + 1

def nodes_value(node):
    global cnt
    if node < n + 1:
        nodes_value(node * 2)
        cnt += 1
        values[node] = cnt
        nodes_value(node * 2 + 1)


T = int(input())
for tc in range(T):
    n = int(input())

    values = [0] * (n + 1)
    cnt = 0
    nodes_value(1)

    print("#{} {} {}".format(tc + 1, values[1], values[n // 2]))