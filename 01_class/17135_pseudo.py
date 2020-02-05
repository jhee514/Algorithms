# 궁수 3 명을 배치
# 각 턴 마다 궁수 각 1 적수를 없애 => 같은 적을 공격 가능
# 공격 받은 적은 0 으로 바꿔 없앤다
# 궁수와 적의 거리가 d 이하
# 적 가운데 가장 가까운 놈
# 거리가까운 놈 여럿이면 가장 왼쪽 놈 공격
# 턴이 끝나면 적은 아래로 한칸 이동
# 모든 적이 마지막 행을 넘어가면 게임 끝
# 궁수를 n 열 가운데 3개 배치하는데 이 중 가장 많은 적을 죽일 수 있는 적의 수를 출력


# 궁수 3을 배치할 조합을 짜내 => # nums = [i for i in range(n)] 에서 positions combinations(nums, 3)
# maxkilled = 0
# for 조합 in 조합s => # for posis in positions:  # posis = (n1, n2, n3)
# while 적이 있는 동안:
# 적의 위치 파악
# for 궁수 in 궁수s
# min_dis = 100
# for 적 in 적s:  # 젤 왼쪽 놈부터
# if 궁수 에서 적과의 거리가 d 이상이면:
# pass
# else:
# cur_dis < min_dis:
# min_dis = cur_dis
# nearst_enemy.append[적y, 적x]
# nearest 안의 적은 다 없애
# 적들의 위치를 한칸씩 아래로 이동
# max_killed < cur_killed
# max_killed = cur_killed
# 적이 없다면
# return maxkilled


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list(zip(*a)))
