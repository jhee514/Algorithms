def sol(N, K):
    pass


"""
Player X and O are playing a game consisting of N rounds.
A player wins the whole game if they win any three rounds in a row, and their opponent does not.
If neither or both players manage to win three rounds in a row, there is a tie.
Note that the total number of rounds a player has won does not matter.
"""

"""
1. 3연승한 사람이 이긴다
2. 3연승을 둘다 했다면 tie
3. 3연승을 둘다 못해도 tie

슬라이싱을 해서 ooo xxx 가 있는지 유무를 체크
1. 한사람만 있으면 그 사람이 이긴다
2. 둘다 있거나 둘다 없으면 tie
"""


def solution(games):
    if len(games) < 3:
        return "tie"

    is_o = 0
    is_x = 0

    for i in range(len(games)-2):
        if games[i:i+3] == "XXX":
            is_x = 1
        if games[i:i+3] == "OOO":
            is_o = 1

        if (is_o+is_x)==0 or (is_o+is_x)==2:
            return "tie"
        elif is_o:
            return "O"
        else:
            return "X"


"""
SKT_FE 01
"""