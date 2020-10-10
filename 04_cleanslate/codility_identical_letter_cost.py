def sol(N, K):
    pass


"""
You are given a string S.
Deletion of the K-th letter of S costs C[K].
After deleting a letter, the costs of deleting other letters do not change.
...
You want to delete some letters from S to obtain a string without two identical letters next to each other.
What is the minimum total cost of deletions to achieve such a string?
"""

"""
연속되는 같은 알파벳 지우는데 드는 최소 비용

1. 연속되는 알파벳의 범위 찾기
2. costs에서 그만큼 리스트를 슬라이싱
3. min 값을 찾아서 sum-min 값이 cost
how to know 연속된 글

"""

def solution(string, costs):
    ans = 0
    i = 0
    while i < len(string)-1:
        if string[i] == string[i+1]:
            j = i
            while j < len(string) and string[i] == string[j]:
                j += 1
            temp_cost = costs[i:j]
            ans += sum(temp_cost) - max(temp_cost)
            i = j
        else:
            i += 1

    return ans

print(solution('abccbd', [0, 1, 2, 3, 4, 5]))


"""
Naver_Intern 03
SKT_FE 04
"""