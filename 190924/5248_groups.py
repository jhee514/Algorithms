import sys
sys.stdin = open("input_5248.txt", "r")

"""
data 를 set 시켜서 출석부랑 비교하고 차집합 원소 수 만큼이 cnt

list 들어오면
두 요소 값을 find(x), find(y) 하고 없으면 make(x) 해서 union(x, y) 해준다.
    find 가 둘다 없으면 하나의 셋 만들어서 넣고
    하나만 없으면 있는데 넣고
    둘다 있으면 합쳐주고
"""

def find(x):
    for g in range(len(group)):
        if x in group[g]:
            return g
    return None


T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    people = set(list(range(1, n+1)))
    cnt = len(people - set(data))

    group = []
    for i in range(len(data)//2):
        if find(data[i*2])!= None and find(data[i*2+1])!= None:
            if find(data[i * 2]) != find(data[i * 2 + 1]):
                group[find(data[i * 2])].update(group.pop(find(data[i * 2 + 1])))
        elif find(data[i*2]) != None:
            group[find(data[i * 2])].add(data[i*2+1])
        elif find(data[i*2+1])!= None:
            group[find(data[i * 2+1])].add(data[i*2])
        else:
            group.append(set([data[i*2], data[i*2+1]]))
    print("#{} {}".format(tc+1, cnt+len(group)))
