def solution(board, skill):
    answer = 0
    N, M = len(board), len(board[0])
    total_skill = [[0]*M for _ in range(N)]
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree *= -1
        
        total_skill[r1][c1] += degree
        A = c2+1 < M
        B = r2+1 < N
        if A:
            total_skill[r1][c2+1] -= degree
        if B:
            total_skill[r2+1][c1] -= degree
        if A & B:
            total_skill[r2+1][c2+1] += degree
    
    for i in range(N):
        for j in range(1, M):
            total_skill[i][j] += total_skill[i][j-1]
    
    for i in range(1, N):
        for j in range(M):
            total_skill[i][j] += total_skill[i-1][j]
    
    for i in range(N):
        for j in range(M):
            board[i][j] += total_skill[i][j]
            if 0 < board[i][j]:
                answer += 1
                
    return answer


board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
board = [[1,2,3],[4,5,6],[7,8,9]]
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
print(solution(board, skill))