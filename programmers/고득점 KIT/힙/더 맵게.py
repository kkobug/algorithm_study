"""
https://programmers.co.kr/learn/courses/30/lessons/42626
"""
from heapq import heappop, heappush, heapify


def solution(scoville, K):
    answer = 0
    
    def is_over_k(food_list, k):
        low = heappop(food_list)
        if k <= low:
            return True # 가장 스코빌이 낮은 음식이 k보다 큼
        heappush(food_list, low)
        return False
    
    heapify(scoville)
    
    if is_over_k(scoville, K):
        return answer
    
    while 1 < len(scoville):
        answer += 1
        new_food = heappop(scoville)
        new_food += 2*heappop(scoville)
        heappush(scoville, new_food)
        
        if is_over_k(scoville, K):
            return answer
    
    if is_over_k(scoville, K):
        return answer
    
    answer = -1
    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([12, 10, 9, 3, 2, 1], 7))
