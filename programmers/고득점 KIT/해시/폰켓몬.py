"""
https://school.programmers.co.kr/learn/courses/30/lessons/1845
"""
def solution(nums):
    answer = 0
    target = len(nums)//2
    poket = set()

    for number in nums:
        if number in poket:
            continue
        answer += 1
        poket.add(number)
        if answer == target:
            break

    return answer


print(solution([3, 1, 2, 3]))
print(solution([3, 3, 3, 2, 2, 4]))
print(solution([3, 3, 3, 2, 2, 2]))
