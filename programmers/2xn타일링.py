"""
https://programmers.co.kr/learn/courses/30/lessons/12900
"""
def solution(n):
    answer = 0
    tile = [1, 2]
    for i in range(2, n):
        tile.append((tile[i-1] + tile[i-2]) % 1000000007)
    answer = tile[-1]
    return answer

print(solution(600))