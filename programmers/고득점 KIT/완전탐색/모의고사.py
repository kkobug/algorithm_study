"""
https://school.programmers.co.kr/learn/courses/30/lessons/42840
"""
def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt = [0, 0, 0]
    for i in range(len(answers)):
        if a[i%5] == answers[i]:
            cnt[0] += 1
        if b[i%8] == answers[i]:
            cnt[1] += 1
        if c[i%10] == answers[i]:
            cnt[2] += 1
    temp = max(cnt)
    for i in range(3):
        if cnt[i] == temp:
            answer.append(i+1)
    return answer


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
