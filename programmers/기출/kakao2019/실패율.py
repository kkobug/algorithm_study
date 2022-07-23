"""
https://school.programmers.co.kr/learn/courses/30/lessons/42889
"""
def solution(N, stages):
    answer = []
    user_in_stage = [0]*(N+2)
    total_user = [0]*(N+2)
    for stage in stages:
        user_in_stage[stage] += 1

    total_user[N+1] = user_in_stage[N+1]

    for i in range(N, 0, -1):
        total_user[i] = user_in_stage[i] + total_user[i+1]

    sorted_user = []
    for i in range(1, N+1):
        if total_user[i] == 0:
            sorted_user.append([0, i])
        else:
            sorted_user.append([user_in_stage[i]/total_user[i], i])

    sorted_user.sort(key=lambda x:(-x[0], x[1]))
    for s in sorted_user:
        answer.append(s[1])

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
