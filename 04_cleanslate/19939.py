"""
n개의 공 k개의 바구니
최소 1개씩 가지고
공의 개수는 모두 달라야 하므로
앞에서부터 1, 2, 3, ... 개씩 넣어줘
이 때 공의 수가 모자라면 실패

"""

def solution(n, k):
    balls = n
    basket = [0] * k
    # 모든 바구니가 최소 1개의 공을 가져야
    for i in range(k):
        basket[i] += (i+1)
        if sum(basket) > n:
            return -1
    balls -= sum(basket)
    while balls:
        for j in range(k-1, -1, -1):
            if balls:
                basket[j] += 1
                balls -= 1
            else:
                break
    return basket[-1] - basket[0]


n, k = map(int, input().split())
solution(n, k)