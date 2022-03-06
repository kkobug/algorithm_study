def solution(n, computers):
    answer = 0
    check = [False] * n
    
    for i in range(n):
        if check[i]:
            continue
        answer += 1
        
        stack = [i]
        check[i] = True
        visit = [False] * n
        visit[i] = True
        while stack:
            k = stack.pop()
            for j in range(n):
                if j == k:
                    continue
                if computers[k][j] and not visit[j]:
                    stack.append(j)
                    check[j] = True
                    visit[j] = True
    return answer


sample_n = [3, 3]
sample_computers = [[[1, 1, 0], [1, 1, 0], [0, 0, 1]], [[1, 1, 0], [1, 1, 1], [0, 1, 1]]]
for i in range(2):
    print(solution(sample_n[i], sample_computers[i]))