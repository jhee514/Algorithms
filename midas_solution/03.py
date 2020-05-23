




def solution(input):
    answer = 0
    def move(data):
        n = len(data)
        for j in range(n):
            nums = []
            for i in range(n-1, -1, -1):
                nums.append(data[i][j])
            temp = []
            for num in nums:
                if num != 0:
                    temp.append(num)
            temp += [0]*(n-len(temp))

            for i in range(n-1, -1, -1):
                data[i][j] = temp[n-i-1]

        return data

    def cnt(data):
        n = len(data)
        total = 0
        for i in range(n):
            for j in range(n):
                if data[i][j]:
                    total += 1
        return total

    def crush(data):
        n = len(data)
        temp_score = 0
        for candy in range(1, 5):
            same = [[0] * n for _ in range(n)]
            for ii in range(n):
                for jj in range(n - 3 + 1):
                    if data[ii][jj:jj + 3] == [candy] * 3:
                        for s in range(3):
                            same[ii][jj+s] = 1

                    temp = [0] * 3
                    for jjj in range(3):
                        temp[jjj] = data[jj+jjj][ii]
                    if temp == [candy] * 3:
                        for jjjj in range(3):
                            same[jj + jjjj][ii] = 1

            for i in range(n):
                for j in range(n):
                    if same[i][j] == 1:
                        data[i][j] = 0
            temp_score += cnt(same)
        return temp_score, data

    n = len(input)
    for i in range(n-1, -1, -1):
        for j in range(n):
            import copy
            board = copy.deepcopy(input)
            if [i, j] == [3, 3]:
                print(answer)
            score = 1
            board[i][j] = 0
            while 1:
                board = move(board)
                temp_score, board = crush(board)
                if temp_score == 0:
                    break
                if temp_score>0:
                    score += temp_score
            if score > answer:
                answer = score
    return answer

data = 	[[1, 1, 3, 3], [4, 1, 3, 4], [1, 2, 1, 1], [2, 1, 3, 2]]
print(solution(data))