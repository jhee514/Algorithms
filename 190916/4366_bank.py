import sys

sys.stdin = open("input_4366.txt", "r")

"""
경우의 수를 모두 볼 것이 아니라
이진수를 바꾼 경우에서 나올 수 있는 십진수로 한정한 범위에서
삼진수의 상태를 보면 된다
"""


"""
각각 한자리씩 바뀌어야 하니까
이진수가 하나 바뀔 때마다 삼진수 가 모두 바뀌는 경우를 비교하면서
같은 값이 나올 때 해당 십진수값을 리턴
"""

def bi_dec(bi):
    result = 0
    for i in range(len(bi)):
        result += int(bi[i]) * 2 ** (len(bi) - 1 - i)
    return result


def ter_dec(ter):
    result = 0
    for i in range(len(ter)):
        result += int(ter[i]) * 3 ** (len(ter) - 1 - i)
    return result


T = int(input())
for tc in range(T):
    n = input()
    m = input()

    for i in range(len(n)):
        for j in range(2):
            if int(n[i]) == j:
                continue
            else:
                temp = ''
                for l in range(len(n)):
                    if l == i:
                        temp += str(j)
                    else:
                        temp += n[l]
                bi = bi_dec(temp)
                for ii in range(len(m)):
                    for jj in range(3):
                        if int(m[ii]) == jj:
                            continue
                        else:
                            tt = ''
                            for ll in range(len(m)):
                                if ll == ii:
                                    tt += str(jj)
                                else:
                                    tt += m[ll]
                            ter = ter_dec(tt)
                            if ter == bi:
                                print("#{} {}".format(tc + 1, ter))
                                break
