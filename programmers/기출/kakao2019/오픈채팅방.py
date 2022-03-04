"""
https://programmers.co.kr/learn/courses/30/lessons/42888
"""
def solution(record):
    answer = []
    IDcheck = dict()
    for i in range(len(record)-1, -1, -1):
        record[i] = record[i].split(" ")
        if record[i][0] == "Change" or record[i][0] == "Enter":
            if IDcheck.get(record[i][1]):
                continue
            IDcheck[record[i][1]] = record[i][2]
    
    for i in range(len(record)):
        if record[i][0] == "Enter":
            answer.append(f'{IDcheck.get(record[i][1])}님이 들어왔습니다.')
        elif record[i][0] == "Leave":
            answer.append(f'{IDcheck.get(record[i][1])}님이 나갔습니다.')
    
    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo",
          "Leave uid1234", "Enter uid1234 Prodo",
          "Change uid4567 Ryan"]
print(solution(record))