import sys
sys.stdin = open("input_4047.txt", "r")


# def find(data):
#     patterns = {"S": [], "D": [], "H": [], "C": []}
#
#     n = len(data) // 3
#     for i in range(n):
#         if int(data[i * 3 + 1:(i + 1) * 3]) in patterns[data[i * 3]]:
#             return "ERROR"
#         else:
#             patterns[data[i * 3]] +=[int(data[i * 3 + 1:(i + 1) * 3])]
#
#     result = []
#     for i in patterns.values():
#         result.append(13 - len(i))
#     return ' '.join(map(str, result))
# ######################################################################################
#
# def find(data):
#     patterns = {"S": 0, "D": 1, "H": 2, "C": 3}
#     cards = [[0]*13 for _ in range(4)]
#
#     n = len(data) // 3
#     for i in range(n):
#         if cards[patterns[data[i * 3]]][int(data[i * 3 + 1:(i + 1) * 3]) - 1] == 1:
#             return "ERROR"
#         else:
#             cards[patterns[data[i*3]]][int(data[i*3+1:(i+1)*3])-1] += 1
#
#     z_count = [0] * 4
#     for i in range(4):
#         for j in range(13):
#             if cards[i][j] == 0:
#                 z_count[i] += 1
#     return ' '.join(map(str, z_count))

########################################################################################

def find(data):
    cards = [[0] * 13 for _ in range(4)]
    n = len(data) // 3
    for i in range(n):
        if data[i * 3] == "S":
            row = 0
        elif data[i * 3] == "D":
            row = 1
        elif data[i * 3] == "H":
            row = 2
        elif data[i * 3] == "C":
            row = 3
        if cards[row][int(data[i * 3 + 1:(i + 1) * 3]) - 1] == 1:
            return "ERROR"
        else:
            cards[row][int(data[i * 3 + 1:(i + 1) * 3]) - 1] += 1
    z_count = [0] * 4
    for i in range(4):
        for j in range(13):
            if cards[i][j] == 0:
                z_count[i] += 1
    return ' '.join(map(str, z_count))

T = int(input())
for t in range(T):
    data = input()
    print("#{} {}".format(t+1, find(data)))