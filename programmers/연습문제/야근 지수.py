"""
https://programmers.co.kr/learn/courses/30/lessons/12927
"""
from heapq import heappop, heappush, heapify

def solution(n, works):
    negative_works = [-i for i in works]
    heapify(negative_works)
    
    for i in range(n):
        k = heappop(negative_works)
        if k == -1:
            if len(negative_works) == 0:
                break
            continue
        else:
            heappush(negative_works, k+1)

    answer = 0
    for work in negative_works:
        answer += work**2
    return answer

print(solution(4, [4, 3, 3]))
print(solution(1, [2, 1, 2]))
print(solution(3, [1, 1]))
x = [50000 for _ in range(20000)]
print(solution(1000000, x))