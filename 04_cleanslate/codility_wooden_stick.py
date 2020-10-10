def sol(N, K):
    pass


"""
There are two wooden sticks of lengths A and B respectively.
Each of them can be cut into shorter sticks of integer lengths.
Our goal is to construct the largest possible square.
In order to do this, we want to cut the sticks in such a way as to achieve 
four sticks of the same length(note that there can be som leftover pieces).
What is the longest side of square that we can achieve?
"""


def solution(a, b):
    if (a+b) < 4:
        return 0

    each_len = [0] * 5

    for i in range(5):
        if i == 0:
            each_len[i] = b//4
        elif i == 4:
            each_len[i] = a//4
        else:
            if (a//i)==0 or (b//(4-i))==0:
                each_len[i] = -1
            else:
                each_len[i] = min([a//i, b//(4-i)])

    longer = 1
    for ii in range(5):
        if each_len[ii] == -1:
            pass
        if each_len[ii] > longer:
            longer = each_len[ii]

    return longer


"""
SKT_FE 03
"""