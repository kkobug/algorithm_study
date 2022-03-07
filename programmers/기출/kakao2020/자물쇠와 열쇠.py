"""
https://programmers.co.kr/learn/courses/30/lessons/60059
"""
from copy import deepcopy as dc
def solution(key, lock):
    M = len(key)
    N = len(lock)
    extend_lock = [[-1]*(2*M+N-2) for _ in range(2*M+N-2)]
    for i in range(N):
        for j in range(N):
            extend_lock[i+M-1][j+M-1] = lock[i][j]
    def match(ext_i, ext_j, K, EL):
        for i in range(M):
            for j in range(M):
                if 0 <= ext_i+i < 2*M+N-2 and 0 <= ext_j+j < 2*M+N-2:
                    EL[ext_i+i][ext_j+j] += K[i][j]
        for i in range(M-1, N+M-1):
            for j in range(M-1, N+M-1):
                if EL[i][j] != 1:
                    return False
        return True
    
    def rotate_90(two_D_list):
        new_N = len(two_D_list)
        ret = [[0]*new_N for _ in range(new_N)]
        for i in range(new_N):
            for j in range(new_N):
                ret[i][j] = two_D_list[new_N-j-1][i]
        return ret
    
    for i in range(M+N-1):
        for j in range(M+N-1):
            if match(i, j, dc(key), dc(extend_lock)):
                return True
    key = rotate_90(key)
    for i in range(M+N-1):
        for j in range(M+N-1):
            if match(i, j, dc(key), dc(extend_lock)):
                return True
    key = rotate_90(key)
    for i in range(M+N-1):
        for j in range(M+N-1):
            if match(i, j, dc(key), dc(extend_lock)):
                return True
    key = rotate_90(key)
    for i in range(M+N-1):
        for j in range(M+N-1):
            if match(i, j, dc(key), dc(extend_lock)):
                return True
    return False

key_list = [
    [[0, 0, 0], [1, 0, 0], [0, 1, 1]],
    [[0, 0, 1], [0, 0, 0], [1, 0, 1]],
    [[1, 1, 0], [0, 0, 1], [0, 0, 0]],
    [[1, 1], [1, 1]],
]
lock_list = [
    [[1, 1, 1], [1, 1, 0], [1, 0, 1]],
    [[0, 1, 1], [1, 1, 1], [0, 1, 0]],
    [[1, 0, 1], [1, 0, 1], [1, 0, 1]],
    [[1, 1, 1], [1, 0, 0], [1, 0, 0]],
]
for KL in range(4):
    print(solution(key_list[KL], lock_list[KL]))