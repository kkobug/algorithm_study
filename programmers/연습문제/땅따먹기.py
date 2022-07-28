"""
https://school.programmers.co.kr/learn/courses/30/lessons/12913
"""
def solution(land):
    n, m = len(land), len(land[0])
    for i in range(1, n):
        for j in range(m):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
    return max(land[-1])


print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))
