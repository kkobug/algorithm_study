def high(idx=0, cnt=0):
    global ans
    if ans == 0:
        return
    if B <= cnt:
        ans = min(ans, cnt-B)
        return
    if idx >= N:
        return

    high(idx+1, cnt+top[idx])
    high(idx+1, cnt)


for tc in range(int(input())):
    N, B = map(int, input().split())
    top = list(map(int, input().split()))
    ans = 200000 - B
    high()
    print(f'#{tc+1} {ans}')