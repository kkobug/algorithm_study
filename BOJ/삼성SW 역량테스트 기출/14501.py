"""
<퇴사>
https://www.acmicpc.net/problem/14501
"""
def talk(idx=0, cnt=0):
    global ans
    if N <= idx or N < idx + date[idx][0]:
        if cnt > ans:
            ans = cnt

    for i in range(idx, N):
        if i < N < i + date[i][0]:
            continue
        talk(i+date[i][0], cnt+date[i][1])


N = int(input())
date = [list(map(int, input().split())) for _ in range(N)]
ans = 0
talk()
print(ans)
