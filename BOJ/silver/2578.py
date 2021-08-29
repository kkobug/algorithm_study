"""
빙고보드와 숫자가 주어질 때, 몇 번째 숫자를 부를 때 빙고 3개가 완성되는지 출력하시오

입력
첫째 줄부터 다섯째 줄까지 빙고판에 쓰여진 수가 가장 위 가로줄부터 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다.\
여섯째 줄부터 열째 줄까지 사회자가 부르는 수가 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다.
빙고판에 쓰여진 수와 사회자가 부르는 수는 각각 1부터 25까지의 수가 한 번씩 사용된다.

출력
첫째 줄에 사회자가 몇 번째 수를 부른 후 철수가 "빙고"를 외치게 되는지 출력한다.

예제 입력 1
11 12 2 24 10
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18
5 10 7 16 2
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15
예제 출력 1
15
"""
def isbingo():
    cnt = 10

    for _ in range(3):
        nums = list(map(int, input().split()))
        for k in nums:
            cnt += 1
            ans = 0
            for i in range(5):
                for j in range(5):
                    if board[i][j] == k:
                        board[i][j] = 0

            for r in range(5):
                if sum(board[r]) == 0:
                    ans += 1
            for c in range(5):
                if board[0][c] + board[1][c] + board[2][c] + board[3][c] + board[4][c] == 0:
                    ans += 1
            if board[0][0] + board[1][1] + board[2][2] + board[3][3] + board[4][4] == 0:
                ans += 1
            if board[0][4] + board[1][3] + board[2][2] + board[3][1] + board[4][0] == 0:
                ans += 1

            if ans >= 3:
                return cnt

    return cnt


board = [list(map(int, input().split())) for _ in range(5)]
for _ in range(2):
    nums = list(map(int, input().split()))
    for k in nums:
        for i in range(5):
            for j in range(5):
                if board[i][j] == k:
                    board[i][j] = 0

print(isbingo())
