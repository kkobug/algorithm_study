"""
https://programmers.co.kr/learn/courses/30/lessons/64064
"""
def solution(user_id, banned_id):
    answer = 0
    answer_list = set()
    def match(origin, hidden):
        if len(origin) != len(hidden):
            return False
        for k in range(len(origin)):
            if hidden[k] == '*':
                continue
            if origin[k] == hidden[k]:
                continue
            return False
        return True
    
    def find(x, answer_id):
        if x == len(banned_id):
            answer_list.add(tuple(answer_id))
            return

        for j in range(len(answer_sheet[x])):
            if answer_id[j]:
                continue
            if answer_sheet[x][j]:
                answer_id[j] = True
                find(x+1, answer_id)
                answer_id[j] = False
    
    answer_sheet = [[False]*len(user_id) for _ in range(len(banned_id))]
    for i in range(len(banned_id)):
        banned = banned_id[i]
        for j in range(len(user_id)):
            user = user_id[j]
            answer_sheet[i][j] = match(user, banned)
    
    find(0, [False]*len(answer_sheet[0]))
    answer = len(answer_list)
    
    return answer

user_ids = [
    ["frodo", "fradi", "crodo", "abc123", "frodoc"],
    ["frodo", "fradi", "crodo", "abc123", "frodoc"],
    ["frodo", "fradi", "crodo", "abc123", "frodoc"]
]
banned_ids = [
    ["fr*d*", "abc1**"],
    ["*rodo", "*rodo", "******"],
    ["fr*d*", "*rodo", "******", "******"]
]
for ids in range(3):
    print(solution(user_ids[ids], banned_ids[ids]))