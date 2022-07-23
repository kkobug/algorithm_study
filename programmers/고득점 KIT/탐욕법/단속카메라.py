"""
https://programmers.co.kr/learn/courses/30/lessons/42884
"""
def solution(routes):
    answer = 0
    idx = -30000
    routes.sort(key=lambda x: x[1])

    for r in routes:
        if r[0] <= idx:
            continue
        answer += 1
        idx = r[1]

    return answer


print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))
