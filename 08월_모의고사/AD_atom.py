import sys

sys.stdin = open("input_atom2.txt", 'r')
import time

start = time.time()

# 상0 하1 좌2 우3
# curr = data[i]
# x = curr[0]
# y = curr[1]
# dir = curr[2]
# energy = curr[3]
#
# def find(atoms):
#     total = 0
#     dx = [0, 0, -1, 1]
#     dy = [1, -1, 0, 0]
#
#     data = deque(atoms)
#
#     for t in range(1, 4002):
#         visited = []
#         while data:
#             if data[0] in visited:
#                 break
#             else:
#                 curr = data.popleft()
#                 sp = [0] * len(data)
#                 for j in range(len(data)):
#                     next = data[j]
#                     if curr[0] + dx[curr[2]] * t * 0.5 == next[0] + dx[next[2]] * t * 0.5 and curr[1] + dy[
#                         curr[2]] * t * 0.5 == next[1] + dy[next[2]] * t * 0.5:
#                         sp[j] = 1
#                 if sum(sp):
#                     total += curr[3]
#                     n_sp = len(sp)
#                     for i in range(n_sp - 1, -1, -1):
#                         if sp[i] == 1:
#                             total += data[i][3]
#                             data.remove(data[i])
#                             n_sp -= 1
#                 else:
#                     data.append(curr)
#                     visited.append(curr)
#         else:
#             break
#     return total
#
#
# T = int(input())
# for tc in range(T):
#     n = int(input())
#     atoms = [list(map(int, input().split())) for _ in range(n)]
#     print("#%d %d" % (tc + 1, find(atoms)))

######################################################
# time : 0.10175704956054688 / (17/50)
#
# def find(data):
#     total = 0
#     dx = [0, 0, -1, 1]
#     dy = [1, -1, 0, 0]
#
#     for t in range(1, 4002):
#         visited = []
#         while data:
#             if data[0] in visited:
#                 break
#             else:
#                 curr = data.pop(0)
#                 sp = []
#                 for j in data:
#                     if curr[0] + dx[curr[2]] * t * 0.5 == j[0] + dx[j[2]] * t * 0.5 and curr[1] + dy[curr[2]] * t * 0.5 == j[1] + dy[j[2]] * t * 0.5:
#                         sp.append(j)
#                 if sp:
#                     total += curr[3]
#                     for i in range(len(sp)):
#                         total += sp[i][3]
#                         data.remove(sp[i])
#                 else:
#                     data.append(curr)
#                     visited.append(curr)
#         else:
#             break
#     return total
#
# T = int(input())
# for tc in range(T):
#     n = int(input())
#     data = [list(map(int, input().split())) for _ in range(n)]
#     print("#%d %d" % (tc+1, find(data)))
#
# print("time :", time.time() - start)

########################################################################################
# time : 0.15082883834838867 / (29/50)

# def find():
#     total = 0
#     dx = [0, 0, -1, 1]
#     dy = [1, -1, 0, 0]
#     visited = [0] * n
#     result = 0
#     for t in range(4002):
#         temp = [0] * n
#         for a1 in range(n-1):
#             if not visited[a1]:
#                 for a2 in range(a1 + 1, n):
#                     if not visited[a2]:
#                         if (data[a1][0] + dx[data[a1][2]]* t * 0.5) == (data[a2][0] + dx[data[a2][2]]* t * 0.5) and (data[a1][1] + dy[data[a1][2]]* t * 0.5) == (data[a2][1] + dy[data[a2][2]]* t * 0.5):
#                             temp[a1] = 1
#                             temp[a2] = 1
#         for tmp in range(n):
#             if temp[tmp]:
#                 visited[tmp] = 1
#                 result += data[tmp][3]
#     print("calc time :", time.time() - start)
#
#     return result
#
# T = int(input())
# for tc in range(T):
#     n = int(input())
#     data = [list(map(int, input().split())) for _ in range(n)]
#     print("data time :", time.time() - start)
#
#     print("#%d %d" % (tc+1, find()))


################################################################################################
# time : 0.3936760425567627
#
# def find():
#     total = 0
#     dx = [0, 0, -1, 1]
#     dy = [1, -1, 0, 0]
#     visited = [0] * n
#     result = 0
#     for t in range(4002):
#         visited = [0] * n
#
#         for a1 in range(n-1):
#             if not visited[a1]:
#                 for a2 in range(a1 + 1, n):
#                     if not visited[a2]:
#                         if (data[a1][0] + dx[data[a1][2]]* t * 0.5) == (data[a2][0] + dx[data[a2][2]]* t * 0.5) and (data[a1][1] + dy[data[a1][2]]* t * 0.5) == (data[a2][1] + dy[data[a2][2]]* t * 0.5):
#                             result += data[a2][3]
#                             visited[a2] = 1
#                             visited[a1] = 1
#             if visited[a1]:
#                 result += data[a1][3]
#     return result
#
# T = int(input())
# for tc in range(T):
#     n = int(input())
#     data = [list(map(int, input().split())) for _ in range(n)]
#     print("#%d %d" % (tc+1, find()))
#
# print("time :", time.time() - start)

################################################################################################
# total time : 0.09804224967956543 (31/50)
# data[i][0] == x.point
# data[i][1] == y.point
# data[i][2] == dx
# data[i][3] == dy
# data[i][4] == energy



# def find():
#     result = 0
#     visited = [0] * n
#     for t in range(4000):
#         if sum(visited) < n - 1:
#             for d in range(n):
#                 if visited[d] == 0:
#                     if data[d][2] == 0:
#                         data[d][1] += data[d][3] * 0.5
#                         if -1000 > data[d][1] or 1000 < data[d][1]:
#                             visited[d] = 1
#                     else:
#                         data[d][0] += data[d][2] * 0.5
#                         if -1000 > data[d][0] or 1000 < data[d][0]:
#                             visited[d] = 1
#             for i in range(n):
#                 ii = 0
#                 if visited[i] == 0:
#                     for j in range(i + 1, n):
#                         if visited[j] == 0:
#                             if data[i][0] == data[j][0] and data[i][1] == data[j][1]:
#                                 ii += 1
#                                 visited[j] = 1
#                                 result += data[j][4]
#                 if ii != 0:
#                     visited[i] = 1
#                     result += data[i][4]
#     return result
#
#
# T = int(input())
# for tc in range(T):
#     n = int(input())
#     raw = [list(map(int, input().split())) for _ in range(n)]
#     data = [[0] * 5 for _ in range(n)]
#     for r in range(n):
#         data[r][0] = raw[r][0]
#         data[r][1] = raw[r][1]
#         data[r][4] = raw[r][3]
#         if raw[r][2] == 0:
#             data[r][2], data[r][3] = 0, 1
#         elif raw[r][2] == 1:
#             data[r][2], data[r][3] = 0, -1
#         elif raw[r][2] == 2:
#             data[r][2], data[r][3] = -1, 0
#         elif raw[r][2] == 3:
#             data[r][2], data[r][3] = 1, 0
#     print("#%d %d" % (tc + 1, find()))

################################################################################################
# total time : 0.07697081565856934 (34/50)
#
# def find():
#     dx = [0, 0, -1, 1]
#     dy = [1, -1, 0, 0]
#     result = 0
#     visited = [0] * n
#     for t in range(3999):
#         if sum(visited) < n - 1:
#             for d in range(n):
#                 if visited[d] == 0:
#                     data[d][0], data[d][1] = data[d][0]+0.5*dx[data[d][2]], data[d][1]+0.5*dy[data[d][2]]
#                     if -1000 > data[d][0] or 1000 < data[d][0] or -1000 > data[d][1] or 1000 < data[d][1]:
#                         visited[d] = 1
#             for i in range(n-1):
#                 ii = 0
#                 if visited[i] == 0:
#                     for j in range(i + 1, n):
#                         if visited[j] == 0:
#                             if data[i][0] == data[j][0] and data[i][1] == data[j][1]:
#                                 ii += 1
#                                 visited[j] = 1
#                                 result += data[j][3]
#                 if ii != 0:
#                     visited[i] = 1
#                     result += data[i][3]
#     return result
#
#
# T = int(input())
# for tc in range(T):
#     n = int(input())
#     data = [list(map(int, input().split())) for _ in range(n)]
#     print("#%d %d" % (tc + 1, find()))

#############################################################################################################
# total time : 0.07685208320617676 (35 /50)
# total time : 0.07302618026733398

# def find():
#     result = 0
#     visited = [0] * n
#     for t in range(4000):
#         if sum(visited) < n-1:
#             for d in range(n):
#                 if visited[d] == 0:
#                     data[d][0] += data[d][2] * 0.5
#                     data[d][1] += data[d][3] * 0.5
#                     if -1000 > data[d][0] or 1000 < data[d][0] or -1000 > data[d][1] or 1000 < data[d][1]:
#                         visited[d] = 1
#             for i in range(n-1):
#                 ii = 0
#                 if visited[i] == 0:
#                     for j in range(i+1, n):
#                         if visited[j] == 0:
#                             if data[i][0] == data[j][0] and data[i][1] == data[j][1]:
#                                 ii = 1
#                                 visited[j] = 1
#                                 result += data[j][4]
#                     if ii == 1:
#                         result += data[i][4]
#                         visited[i] = 1
#
#     return result
#
#
# T = int(input())
# for tc in range(T):
#     n = int(input())
#     raw = [list(map(int, input().split())) for _ in range(n)]
#     data = [[0] * 5 for _ in range(n)]
#     for r in range(n):
#         data[r][0] = raw[r][0]
#         data[r][1] = raw[r][1]
#         data[r][4] = raw[r][3]
#         if raw[r][2] == 0:
#             data[r][2], data[r][3] = 0, 1
#         elif raw[r][2] == 1:
#             data[r][2], data[r][3] = 0, -1
#         elif raw[r][2] == 2:
#             data[r][2], data[r][3] = -1, 0
#         elif raw[r][2] == 3:
#             data[r][2], data[r][3] = 1, 0
#     print("#%d %d" % (tc + 1, find()))


#############################################################################################################

# def find():
#     result = 0
#     visited = [0] * n
#     for t in range(3999):
#         if sum(visited) < n - 1:
#             for d in range(n):
#                 if visited[d] == 0:
#                     data[d][0] += data[d][2] * 0.5
#                     data[d][1] += data[d][3] * 0.5
#                     if -1000 > data[d][0] or 1000 < data[d][0] or -1000 > data[d][1] or 1000 < data[d][1]:
#                         visited[d] = 1
#             for i in range(n-1):
#                 ii = 0
#                 if visited[i] == 0:
#                     for j in range(i + 1, n):
#                         if visited[j] == 0:
#                             if data[i][0] == data[j][0] and data[i][1] == data[j][1]:
#                                 ii += 1
#                                 visited[j] = 1
#                                 result += data[j][4]
#                 if ii != 0:
#                     visited[i] = 1
#                     result += data[i][4]
#     return result
#
#
# T = int(input())
# for tc in range(T):
#     n = int(input())
#     raw = [list(map(int, input().split())) for _ in range(n)]
#     data = [[0] * 5 for _ in range(n)]
#     for r in range(n):
#         data[r][0] = raw[r][0]
#         data[r][1] = raw[r][1]
#         data[r][4] = raw[r][3]
#         if raw[r][2] == 0:
#             data[r][2], data[r][3] = 0, 1
#         elif raw[r][2] == 1:
#             data[r][2], data[r][3] = 0, -1
#         elif raw[r][2] == 2:
#             data[r][2], data[r][3] = -1, 0
#         elif raw[r][2] == 3:
#             data[r][2], data[r][3] = 1, 0
#     print("#%d %d" % (tc + 1, find()))

#############################################################################################################
# jp total time : 0.05176997184753418

# def move_atoms(atoms):
#     directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
#     board = {}
#     collapse = []
#     out_atom = []
#     result = 0
#
#     for atom in atoms:
#         atom[0] += directions[atom[2]][0]
#         atom[1] += directions[atom[2]][1]
#
#         if atom[0] > 2000 or atom[0] < -2000 or atom[1] > 2000 or atom[1] < -2000:
#             out_atom.append(atom)
#         elif (atom[0], atom[1]) not in board.keys():
#             board[(atom[0], atom[1])] = [atom]
#         else:
#             board[(atom[0], atom[1])].append(atom)
#             collapse.append((atom[0], atom[1]))
#
#     if out_atom:
#         for temp in out_atom:
#             atoms.remove(temp)
#
#     if collapse:
#         for key in list(set(collapse)):
#             for atom in board.get(key):
#                 result += atom[3]
#                 atoms.pop(atoms.index((atom)))
#
#     return result
#
#
# T = int(input())
# for t in range(1, T + 1):
#     N = int(input())
#     atoms = [list(map(int, input().split())) for _ in range(N)]
#     is_collapse = True
#     result = 0
#     num = 1
#
#     for atom in atoms:
#         atom[0] *= 2
#         atom[1] *= 2
#         atom.append(num)
#         num += 1
#
#     while len(atoms) > 2:
#         result += move_atoms(atoms)
#
#     print('#{} {}'.format(t, result))

#############################################################################################################
# def solve():
#     N = int(input())
#     nucs = [list(map(int, input().split())) for n in range(N)]
#  
#     candidate = [] # 충돌 가능한 경우들
#     #원자 2개 combination
#     for nuc1_n in range(N - 1):
#         for nuc2_n in range(nuc1_n + 1, N): # (0, 1), ..., (0, N - 1), ..., (N - 2, N - 1)
#             # 충돌 가능한 경우는 같은 x값을 갖고 수직으로 움직이거나
#             # 같은 y값을 갖고 수평으로 움직이거나
#             # 어쩌다 직각으로 충돌하거나
#             dx = nucs[nuc1_n][0] - nucs[nuc2_n][0]
#             dy = nucs[nuc1_n][1] - nucs[nuc2_n][1]
#             d1, d2 = nucs[nuc1_n][2], nucs[nuc2_n][2]
#  
#             if dx == 0: # x값이 같을 때
#                 if dy > 0: # 첫번째 원자가 위쪽에 있다면
#                     if d1 == 1 and d2 == 0: # 첫번째 원자는 아래로, 두번째 원자는 위로
#                         candidate.append([nuc1_n, nuc2_n, abs(dy) / 2])
#                 else: # 첫번째 원자가 아래에 있다면
#                     if d1 == 0 and d2 == 1: # 첫번쨰 원자는 위로, 두번째 원자는 아래로
#                         candidate.append([nuc1_n, nuc2_n, abs(dy) / 2])
#  
#             elif dy == 0: # y값이 같을 때
#                 if dx > 0: # 첫번째 원자가 오른쪽에 있다면
#                     if d1 == 2 and d2 == 3: # 첫번째 원자는 왼쪽, 두번쨰 원자는 오른쪽
#                         candidate.append([nuc1_n, nuc2_n, abs(dx) / 2])
#                 else: # 첫번째 원자가 왼쪽에 있다면
#                     if d1 == 3 and d2 == 2: # 첫번째 원자는 오른쪽, 두번째 원자는 왼쪽
#                         candidate.append([nuc1_n, nuc2_n, abs(dx) / 2])
#  
#             elif dx == dy: # +45도
#                 if dx < 0: # 우, 하 또는 상, 좌 조합일 때 충돌
#                     if (d1 == 3 and d2 == 1) or (d1 == 0 and d2 == 2):
#                         candidate.append([nuc1_n, nuc2_n, abs(dx)])
#                 else: # 좌, 상 또는 하, 우 조합일 때 충돌
#                     if (d1 == 2 and d2 == 0) or (d1 == 1 and d2 == 3):
#                         candidate.append([nuc1_n, nuc2_n, abs(dx)])
#  
#             elif dx == -dy: # -45도
#                 if dx < 0: # 우, 상 또는 하, 좌 조합일 때 충돌
#                     if (d1 == 3 and d2 == 0) or (d1 == 1 and d2 == 2):
#                         candidate.append([nuc1_n, nuc2_n, abs(dx)])
#                 else: # 좌, 하 또는 상, 우 조합일 때 충돌
#                     if (d1 == 2 and d2 == 1) or (d1 == 0 and d2 == 3):
#                         candidate.append([nuc1_n, nuc2_n, abs(dx)])   
#  
#             else: # 충돌 가능성 없는 조합
#                 pass
#     # 충돌 가능성 있는 조합 선정 완료
#     # 충돌 시간을 기준으로 정렬
#     candidate = sorted(candidate, key = lambda x: x[2], reverse = True)
#     existing = [True] * len(nucs)
#     total_energy = 0
#  
#     # # .pop으로 장 먼저 충돌하는 것부터 리스트에서 빼낸다
#     # # 이미 충돌한 원자가 포함되는 경우 무시
#     # # 충돌하면 충돌한 것으로 표시하고 에너지를 총 에너지에 합한다
#     # while candidate:
#     #     nuc1_n, nuc2_n, time = candidate.pop()
#     #     if existing[nuc1_n] == True and existing[nuc2_n] == True:
#     #         total_energy += (nucs[nuc1_n][3] + nucs[nuc2_n][3])
#     #         existing[nuc1_n] = False
#     #         existing[nuc2_n] = False
#  
#     # 동시에 여러 개(특히 홀수 개) 만나는 경우를 고려해야 함
#     # 같은 시간에 충돌하는 원자를 모두 모은다
#     while candidate:
#         loop_time = candidate[-1][2]
#         temp = []
#         try:
#             while loop_time == candidate[-1][2]:
#                 n1, n2, time = candidate.pop()
#                 # 예를 들어 첫 루프에서 1, 2 두번쨰 루프에서 2, 3이 충돌한다면 모두 1, 2, 3이 충돌하는 것
#                 # 공유되는 원자가 있는 것들을 하나의 충돌 이벤트로 묶어야 함
#                 # [[1, 2, 3], [7, 16]] 이런 식으로?
#                 if existing[n1] == False or existing[n2] == False:
#                     continue
#  
#                 flag = False
#                 for cmb in temp: # temp에는 나오는 조합을 저장. 원자가 겹치는 것을 하나의 리스트로 묶어서 리스트로 저장한다.
#                     if n1 in cmb or n2 in cmb: # 이미 있는 경우에 추가하고 (나중에 set으로 겹치는 것 제거)
#                         cmb += [n1, n2]
#                         flag == True
#                     #없으면.... 끝까지 없으면 새 리스트를 추가해야 하는데
#                  
#                 if flag == False:
#                     temp.append([n1, n2])
#         except: pass
#         # 충돌 시간이 같은 원자들을 리스트에 묶어둠
#         temp1 = []
#         for lst in temp:
#             temp1 += lst
#         temp1 = set(temp1)
#         for nuc in temp1:
#             total_energy += nucs[nuc][3]
#             existing[nuc] = False
#  
#      
#     return total_energy
#  
# T = int(input())
# for tc in range(1, T + 1):
#     soln = solve()
#     print("#{} {}".format(tc, soln))
#############################################################################################################
# total time : 0.127000093460083

def find():
    result = 0
    dir = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    for t in range(3999):
        out =[]
        for d in range(len(data)):
            data[d][0] += dir[data[d][2]][0] * 0.5
            data[d][1] += dir[data[d][2]][1] * 0.5
            if -1000 > data[d][0] or 1000 < data[d][0] or -1000 > data[d][1] or 1000 < data[d][1]:
                temp.append(data[d])
        if out:
            for tt in out:
                data.remove(tt)

        temp = []
        visited = [0] * len(data)
        for i in range(len(data)-1):
            if visited[i] == 0:
                ii = 0
                for j in range(i+1, len(data)):
                    if visited[j] == 0:
                        if data[i][0] == data[j][0] and data[i][1] == data[j][1]:
                            ii = 1
                            result += data[j][3]
                            visited[j] = 1
                            temp.append(data[j])
                if ii == 1:
                    result += data[i][3]
                    temp.append(data[i])
        if temp:
            for tmp in temp:
                data.remove(tmp)
    return result

T = int(input())
for tc in range(T):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    print("#%d %d" % (tc + 1, find()))
print("total time :", time.time() - start)