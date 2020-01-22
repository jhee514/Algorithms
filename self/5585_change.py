# input 380
# output 4

price = int(input())


def sol(price):
    coins = [500, 100, 50, 10, 5, 1]
    paid = 1000
    cnt = 0
    change = paid - price

    j = 0
    for i in range(len(coins)):
        while 1:
            if change >= coins[i] * j:
                j += 1
            else:
                j -= 1
                break
        change -= coins[i] * j
        cnt += j
        j = 0

    print(cnt)


sol(price)
