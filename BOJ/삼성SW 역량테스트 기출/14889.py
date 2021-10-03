"""
https://www.acmicpc.net/problem/14889
"""
def game(A=[], idx=0):
    global ans

    if len(A) == N//2:
        B = list(set(range(N)) - set(A))
        temp_a = temp_b = 0
        for r in range(N//2-1):
            for c in range(r+1, N//2):
                temp_a += team[A[r]][A[c]] + team[A[c]][A[r]]
                temp_b += team[B[r]][B[c]] + team[B[c]][B[r]]
        ans = min(abs(temp_a-temp_b), ans)
        return

    for i in range(idx, min(N, idx+N//2+1)):
        A.append(i)
        game(A, i+1)
        A.pop()

N = int(input())
team = [list(map(int, input().split())) for _ in range(N)]
ans = 20000
game()
print(ans)