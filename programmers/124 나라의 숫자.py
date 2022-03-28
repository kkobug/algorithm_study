def solution(n):
    answer = ''
    key = {
        0: '1', 1: '2', 2: '4',
    }

    def change(k):
        nonlocal key
        if k <= 3:
            if k == 3:
                return '4'
            return str(k)
        k -= 1
        return change(k // 3) + key[k % 3]

    answer = change(n)
    return answer

for i in range(1, 11):
    print(solution(i))