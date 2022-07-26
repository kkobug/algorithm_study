def solution(arr, divisor):
    answer = []
    for a in arr:
        if a % divisor:
            continue
        answer.append(a)
    answer.sort() if answer else answer.append(-1)
    return answer


print(solution([5, 9, 7, 10], 5))
print(solution([2, 36, 1, 3], 1))
print(solution([3, 2, 6], 10))
