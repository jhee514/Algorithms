# 2019.10.01 데일리 과제 2
# 재귀 - 문제 6
def find(node, level=0):
    if node:
        if node < 10:
            print(' ', end='')

        print(node, end='')
        if tree[node]:
            for child in range(len(tree[node])):
                if level == 0:
                    if child == 0:
                        print("--+--", end='')
                        find(tree[node][child], level + 1)
                    elif child == len(tree[node]) - 1:
                        print()
                        print("    L--", end='')
                        find(tree[node][child], level + 1)
                    else:
                        print()
                        print("    +--", end='')
                        find(tree[node][child], level + 1)
                else:
                    if child == 0:
                        print("-----", end='')
                        find(tree[node][child], level + 1)
                    elif child == len(tree[node]) - 1:
                        print()
                        print('  ', end='')
                        for _ in range(level):
                            print('       ', end='')
                        print("L----", end='')
                        find(tree[node][child], level + 1)
                    else:
                        print()
                        print('  ', end='')
                        for _ in range(level):
                            print('       ', end='')
                        print("-----", end='')
                        find(tree[node][child], level + 1)


tree = [[0], [2, 3, 4], [5, 6, 7], [], [8, 9], [], [], [], [], [10], [11, 8], [12, 3, 13], [], [14, 15], [], []]
find(1)
