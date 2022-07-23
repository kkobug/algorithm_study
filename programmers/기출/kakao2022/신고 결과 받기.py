"""
https://school.programmers.co.kr/learn/courses/30/lessons/92334
"""
def solution(id_list, report, k):
    answer = []
    user = dict()
    for id in id_list:
        user[id] = [set(), 0]

    for r in report:
        _from, _to = r.split()
        if _to not in user[_from][0]:
            user[_from][0].add(_to)
            user[_to][1] += 1

    for id in id_list:
        cnt = 0
        for reported_user in user[id][0]:
            if k <= user[reported_user][1]:
                cnt += 1
        answer.append(cnt)

    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
