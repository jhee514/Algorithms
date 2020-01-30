# 1

"""
1번
리스트 A 에 있는 단어를 조합을 해서 가장 긴 단어를 만드는데
1. 중복되는 알파벳 없을 것
2. 불가ㄴㅇ하면 0을 리
"""

"""
2번

"""

"""
3번
동전을 앞뒤 차례로 놓고 싶은데 최소한을 뒤집고 ㅅ피다.
몇개를 뒤집는 것이 최솟값일까
0 1 0 0 0 1 0

check 함수
0과 1이 교차로 나오는지 확인

어차피 01010101이거나 10101010이여야 하니까
완벽한 배열 상태와 차이값을 구하는 것

"""

"""
def solution(A):
    def check(s, sample, stand):
        cnt = 0
        for ii in range(s):
            if sample[ii] != stand[ii]:
                cnt += 1
        return cnt


    size = len(A)

    zero_arr = [0] * size
    one_arr = [1] * size
    for i in range(size):
        if i % 2:
            zero_arr[i] = 1
            one_arr[i] = 0

    diff_zero = check(size, A, zero_arr)
    diff_one = check(size, A, one_arr)

    if diff_one > diff_zero:
        return diff_zero
    else:
        return diff_one

A = [1, 0, 1, 0, 1, 1]
print(solution(A))
"""

"""
4번
def solution(A, B):
    mul = A * B
    i = 0
    while mul > 2 ** i:
        i += 1
    for ii in range(i):
"""

"""
1번
조합
단어를 더해
중복 여부 확인
"""

"""
Example test:   ['co', 'dil', 'ity']
OK

Example test:   ['abc', 'yyy', 'def', 'csv']
OK

Example test:   ['potato', 'kayak', 'banana', 'racecar']
OK

Example test:   ['eva', 'jqw', 'tyn', 'jan']
OK
"""

max_len = 0
def check(s):
    for i in range(len(s) - 1):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return False
    return True

def comb(k, l, A, s=''):
        global max_len
        if k == l:
            if max_len < len(s):
                max_len = len(s)
        else:
            if check(s+A[k]):
                comb(k+1, l, A, s+A[k])
            else:
                comb(k+1, l, A, s)

def solution(A):
    comb(0, len(A), A)
    return max_len



"""
도희

def solution(A):
    array = ['']
    res = 0
    for word in A[::-1]: # 사전에 A 배열 글자중 중복된 글자들이 들어있는 값을 제거
        for char in word:
            if word.count(char)>1:
                A.pop(A.index(word))
                break
    			
    while True:
        flag = len(array)
        for i in A:
            for j in array:
                if i not in j:
                    temp = [i+j, j+i]
                    for word in temp:
                        for char in word:
                            if word.count(char) > 1:
                                break
                        else:
                            if word not in array:
                                array += [word]
                                if len(word) > res:
                                    res = len(word)
        if len(array) == flag:
            break
    return res
"""
"""
도희2
import itertools
def solution(A):
    array = []
    for num in range(len(A)):
        array += list(itertools.combinations(A, num))
    res = 0
    for word in array:
        temp = ''.join(word)
        for char in temp:
            if temp.count(char) > 1:
                break
        else:
            if len(temp) > res:
                res = len(temp)
    return res
"""