import sys

sys.stdin = open("input_1258.txt", "r")


# dfs 를 사용해서 0.0 부터 쭉 훝어 내려오는거야
# 0 이 아닌 점을 발견하면 그게 해당 왼쪽 코너(left_corner 로 저장) 점이 되고
# 여기서부터 visited 에 넣어 주고, cnt += 1
# 여기서는 오른쪽으로만 옮겨 가면서 visited 표시 해주고
# 다음 수가 0이면 아래 방향으로 바꿔서 타고 내려가면서 visited 처리 해준다
# 내려가다 다음 수가 0이 아니면 해당 점을 right_point 로 저장해준다
# 해당 범위 내의 점들을 모두 visited 처리 해준다.
# 해당 범위의 크기를 size 리스트에 저장한다.
# size 출력 시 행렬 크기 순서대로 출력
# 크기가 같으면 행이 작은 순서로 출력

# 이걸 계속 돌려서 cnt 올리면 행렬의 개수가 나오고
# size 리스트를 출력

# boundary checked?? => 꼭!!!!!!!!!!!

def find():
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    boxes = []
    for i in range(n):
        for j in range(n):
            if data[i][j] != 0 and not visited[i][j]:
                cnt += 1
                a, b = i, j  # 아래에서 변의 길이를 측정할 때 i, j 값이 필요해서 a, b 로 따로 저장
                # 아니면 garo, sero = 0, 0 이라고 하고 밑에서 garo += 1 씩 해줘도 측정가능
                while b + 1 < n and data[a][b + 1] != 0:
                    b = b + 1
                while a + 1 < n and data[a + 1][b] != 0:
                    a = a + 1
                c, d = a, b
                boxes.append([(c - i + 1) * (d - j + 1), (c - i + 1), (d - j + 1)])
                for p in range(i, c + 1):
                    for q in range(j, d + 1):
                        visited[p][q] = 1
    for i in range(len(boxes) - 1):
        minbox = i
        for j in range(i + 1, len(boxes)):
            if boxes[j][0] < boxes[minbox][0]:
                minbox = j
            if boxes[j][0] == boxes[minbox][0]:
                if boxes[j][1] < boxes[minbox][1]:
                    minbox = j
        boxes[i], boxes[minbox] = boxes[minbox], boxes[i]

    result = [cnt]
    for i in range(len(boxes)):
        result.append(boxes[i][1])
        result.append(boxes[i][2])
    return ' '.join(map(str, result))


T = int(input())
for t in range(T):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    print("#{} {}".format(t + 1, find()))