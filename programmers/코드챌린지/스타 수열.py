"""
https://programmers.co.kr/learn/courses/30/lessons/70130
"""
def solution(a):
    def get_star_sequence(number):
        nonlocal a
        ret = i = 0
        while i < len(a)-1:
            if (a[i] != number and a[i+1] != number) or (a[i] == number and a[i+1] == number):
                i += 1
            else:
                ret += 1
                i += 2
        return ret

    answer = max_number = 0
    reference = dict()
    for i in range(len(a)):
        if max_number < a[i]:
            max_number = a[i]
        if reference.get(a[i]):
            reference[a[i]] += 1
        else:
            reference[a[i]] = 1
    visit = [False] * (len(a))
    visit[max_number] = True
    answer = get_star_sequence(max_number)

    for i in range(len(a)):
        if (reference[a[i]] <= answer) or visit[a[i]]:
            continue
        visit[a[i]] = True
        answer = max(answer, get_star_sequence(a[i]))

    return answer * 2


print(solution([0]))
print(solution([5,2,3,3,5,3]))
print(solution([0,3,3,0,7,2,0,2,2,0]))