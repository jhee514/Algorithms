records = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]

action = {"Enter": "들어왔습니다.", "Leave": "나갔습니다."}
nickname = {}

# 한 바퀴 돌면서 enter, change 에 대한 닉네임을 쫙 정리해
# 다시 한바퀴 돌면서 해당 이름에 대한 출입 기록을 출력

for record in records:
    string = record.split()
    if string[0] == "Enter" or string[0] == "Change":
        nickname[string[1]] = string[2]

for record in records:
    string = record.split()
    if string[0] in action.keys():
        print("{}님이 {}".format(nickname[string[1]], action[string[0]]))
