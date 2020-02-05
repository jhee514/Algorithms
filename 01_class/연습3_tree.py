def inorder_traverse(node):
    if node:
        inorder_traverse(tree[node][0])
        print("%d" % node, end=' ')
        inorder_traverse(tree[node][1])


def postorder_traverse(node):
    if node:
        postorder_traverse(tree[node][0])
        postorder_traverse(tree[node][1])
        print("%d" % node, end=' ')


def preorder_traverse(T):
    if T:
        print("%d" % T, end=' ')
        preorder_traverse(tree[T][0])
        preorder_traverse(tree[T][1])


n = 12
raw = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]

tree = [[0] * 2 for _ in range(n + 1)]
for i in range(11):
    p, c = raw[i * 2], raw[i * 2 + 1]
    if tree[p][0]:
        tree[p][1] = c
    else:
        tree[p][0] = c
print(tree)

preorder_traverse(1)
print()
inorder_traverse(1)
print()
postorder_traverse(1)
