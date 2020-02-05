import sys

sys.stdin = open("input_1231.txt", "r")


def inorder_traverse(node):
    global inorder
    # parent = find_p(node)
    if node:
        inorder_traverse(tree[node][0])
        inorder += data[node-1][1]
        inorder_traverse(tree[node][1])


def postorder_traverse(node):
    global postorder
    if node:
        postorder_traverse(tree[node][0])
        postorder_traverse(tree[node][1])
        postorder += data[node-1][1]


def find_p(node):
    for i in range(len(tree)):
        if tree[i][0] == node or tree[i][1] == node:
            return i


T = 10
for tc in range(T):
    n = int(input())
    data = [list(input().split()) for _ in range(n)]
    tree = [[0]* 2 for _ in range(n+1)]
    for i in data:
        p = int(i[0])
        if len(i) > 2:
            lc = int(i[2])
            tree[p][0] = lc
        if len(i) > 3:
            rc = int(i[3])
            tree[p][1] = rc
    inorder = ''
    postorder = ''
    inorder_traverse(1)
    postorder_traverse(1)
    print("#{} {} {}".format(tc+1, 'in =', inorder))
    print("#{} {} {}".format(tc+1, 'post =', postorder))
