def line(idx=0, cnt=0):
    global ans
    if ans <= cnt:
        return
    if idx == N:
        ans = cnt
    for i in range(N):
        if V[i]: continue
        V[i] = True
        line(idx+1, cnt+F[idx][i])
        V[i] = False


for tc in range(int(input())):
    N = int(input())
    F = [list(map(int, input().split())) for _ in range(N)]
    V = [False] * N
    ans = 1500
    line()
    print(f'#{tc+1} {ans}')
