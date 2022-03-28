"""
https://programmers.co.kr/learn/courses/30/lessons/12971
"""
def det_max(x, y):
    if x < y: return y
    return x

def solution(sticker):
    N = len(sticker)
    
    if N == 1: return sticker[0]
    if N == 2: return det_max(sticker[0], sticker[1])
    
    pick_fir = [0] * N
    pick_sec = [0] * N
    
    pick_fir[0] = pick_fir[1] = sticker[0]
    pick_sec[1] = sticker[1]
    for i in range(2, N-1):
        pick_fir[i] = det_max(pick_fir[i-2] + sticker[i], pick_fir[i-1])
        pick_sec[i] = det_max(pick_sec[i-2] + sticker[i], pick_sec[i-1])
    
    return max(pick_fir[-2], pick_sec[-3] + sticker[-1], pick_sec[-2])

print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
print(solution([1, 3, 2, 5, 4]))
