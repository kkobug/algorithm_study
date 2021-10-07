def delivery(now, T=0, cnt=0):
    global ans
    if ans <= cnt:  # 이동한 거리가 최소가 아니면 가지치기
        return
    if T == N:
        cnt += abs(now[0]-ed[0]) + abs(now[1]-ed[1])  # 마지막에 집으로 돌아가는 거리 계산해주기
        ans = min(ans, cnt)
    for i in range(4, len(dots), 2):
        if visit[i]: continue
        visit[i] = True
        dist = abs(now[0]-dots[i]) + abs(now[1]-dots[i+1])  # 이동한 거리를 가지고 재귀
        delivery((dots[i], dots[i+1]), T+1, cnt+dist)
        visit[i] = False

for tc in range(int(input())):
    N = int(input())
    dots = list(map(int, input().split()))  # 4부터 N개를 2단위로 끊어서
    ed = (dots[2], dots[3])
    visit = [False]*len(dots)
    ans = 10000
    delivery((dots[0], dots[1]))
    print(f'#{tc+1} {ans}')