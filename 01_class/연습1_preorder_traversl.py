## VLR 부모 - 왼쪽자식 - 오른쪽 자식

def find():
    root = 1
    queue = []
    q = []
    q.append(root)
    result = ''

    while q:
        cur = q.pop(0)
        result += str(cur) +' '
        temp=[]
        for i in range(len(arr)):
            if arr[i][0] == cur:
                temp.append(arr[i][1])
        q = temp + q
    return result


def preorder_traverse(T):
    if T :
        print("%d" % T, end=' ')
        preorder_traverse(tree[T][0])
        preorder_traverse(tree[T][1])


n = 13
data = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
nums = list(map(int, data.split()))
arr = [nums[i*2 : i*2+2] for i in range(12)]
print(find())


"""
이진트리이니까 tree[parent][0], tree[parent][1] 이런식으로 부모, 왼쪽자식, 오른쪽 자식을 넣어
"""
tree = [[0] * 2 for _ in range(n+1)]
for i in arr:
    p, c = i[0], i[1]
    if tree[p][0]:
        tree[p][1] = c
    else:
        tree[p][0] = c

print('tree = ', tree)
print(preorder_traverse(1))