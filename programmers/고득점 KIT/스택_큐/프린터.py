"""
https://school.programmers.co.kr/learn/courses/30/lessons/42587
"""
def solution(priorities, location):
    answer = 1
    now_print = sorted(priorities, reverse=True)
    finished = [False] * len(priorities)
    idx = work_idx = 0
    while True:
        if not finished[idx] and now_print[work_idx] == priorities[idx]:
            finished[idx] = True
            if location == idx:
                break
            answer += 1
            work_idx += 1
        idx += 1
        idx %= len(priorities)
    return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
