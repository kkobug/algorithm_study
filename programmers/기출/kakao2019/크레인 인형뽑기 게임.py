"""
https://programmers.co.kr/learn/courses/30/lessons/64061
"""
def solution(board, moves):
    answer = 0
    N = len(board)  # 인형뽑기 기계의 높이
    M = len(board[0])  # 인형뽑기 기계의 폭
    """
    [[0,0,0,0,0],
     [0,0,1,0,3],
     [0,2,5,0,1],
     [4,2,4,4,2],
     [3,5,1,3,1]]
    """
    basket = []  # 바구니
    for m in moves:
        m -= 1
        # 이번에 뽑는건 m열의 어떤 인형
        if board[N-1][m] == 0:
            # 뽑는 줄에 인형이 없으면 아무 일도 일어나지 않습니다.
            continue

        for i in range(N):
            if board[i][m]:
                now = board[i][m]
                board[i][m] = 0
                break
        
        if basket and basket[-1] == now:
                basket.pop()
                answer += 2
        else:
            basket.append(now)
    return answer

print(solution(
    [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],
    [1,5,3,5,1,2,1,4]
))