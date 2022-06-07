"""
https://programmers.co.kr/learn/courses/30/lessons/68646
"""
def solution(a):
    answer = 0
    N = len(a)
    check = set()
    min_value = a[0]
    for i in range(1, N):
        check.add(min_value)
        min_value = min(min_value, a[i])
    min_value = a[-1]
    for i in range(N-2, -1, -1):
        check.add(min_value)
        min_value = min(min_value, a[i])
    answer = len(check)
    return answer


a_list = [
    [9, -1, -5],
    [-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]
]
for a in a_list:
    print(solution(a))