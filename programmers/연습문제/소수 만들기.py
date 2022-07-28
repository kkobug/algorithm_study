"""
https://school.programmers.co.kr/learn/courses/30/lessons/12977
"""
def solution(nums):
    answer = 0
    sieve = [False, False] + [True] * 2999
    for i in range(2, 3000):
        k = 2
        while k * i <= 3000:
            sieve[k*i] = False
            k += 1

    def get_3_number(start_num, selected):
        nonlocal answer
        if len(selected) == 3:
            if sieve[nums[selected[0]] + nums[selected[1]] + nums[selected[2]]]:
                answer += 1
            return

        for i in range(start_num, len(nums)):
            selected.append(i)
            get_3_number(i+1, selected)
            selected.pop()

    get_3_number(0, [])
    return answer


print(solution([1, 2, 3, 4]))
print(solution([1, 2, 7, 6, 4]))
