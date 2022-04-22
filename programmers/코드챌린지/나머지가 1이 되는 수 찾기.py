"""
https://programmers.co.kr/learn/courses/30/lessons/87389
"""
def solution(n):
    answer = 0
    n -= 1
    for i in range(2, 1+n):
        if n % i == 0:
            answer = i
            break
    return answer


n_list = [10, 12]
for i in range(2):
    print(solution(n_list[i]))