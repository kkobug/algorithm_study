"""
https://school.programmers.co.kr/learn/courses/30/lessons/17681
"""
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        temp = ""
        for j in range(n - 1, -1, -1):
            if arr1[i] % 2 or arr2[i] % 2:
                temp = "#" + temp
            else:
                temp = " " + temp

            arr1[i] //= 2
            arr2[i] //= 2
        answer.append(temp)
    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
