def do_work(idx=0, cnt=1.0):
    global ans
    if idx == N:
        ans = cnt*100
        return

    for i in range(N):
        if check[i]: continue
        n_cnt = cnt * work[idx][i]/100
        if n_cnt <= ans/100: continue
        check[i] = True
        do_work(idx+1, n_cnt)
        check[i] = False


for tc in range(int(input())):
    N = int(input())
    work = [list(map(int, input().split())) for _ in range(N)]
    check = [False]*N
    ans = 0
    do_work()
    print(f'#{tc+1} {ans:.6f}')