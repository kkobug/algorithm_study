"""
https://programmers.co.kr/learn/courses/30/lessons/77884
"""
def solution(left, right):
    answer = 0    
    for number in range(left, right+1):
        cnt = 0
        for i in range(1, number+1):
            if number % i:
                continue
            cnt += 1
        
        if cnt % 2:
            answer -= number
        else:
            answer += number
    return answer

print(solution(13, 17))
print(solution(24, 27))
print(solution(400, 400))
