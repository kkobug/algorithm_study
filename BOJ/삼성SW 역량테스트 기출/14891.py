"""
https://www.acmicpc.net/problem/14891
예제 입력
10101111
01111101
11001110
00000010
2
3 -1
1 1
예제 출력
7
"""
G = 4
gear = [list(input()) for _ in range(G)]
st = [2] * G
ed = [6] * G
for _ in range(int(input())):
    N, R = map(int, input().split())
    N -= 1
    is_R = [False] * G
    is_R[N] = True
    for r in range(N + 1, G):  # 순차검사 : 지금 기어의 끝점과 이전 기어의 시작점이 다른가?
        if gear[r][ed[r]] != gear[r - 1][st[r - 1]]:
            is_R[r] = True
        else:
            break
    for r in range(N - 1, -1, -1):  # 역순검사 : 지금 기어의 시작점과 이전 기어의 끝점이 다른가?
        if gear[r][st[r]] != gear[r + 1][ed[r + 1]]:
            is_R[r] = True
        else:
            break

    # 여기부터는 기어 돌리기!
    for r in range(G):
        if not is_R[r]:
            continue
        if N % 2 == r % 2:
            k = -R
        else:
            k = R
        st[r] = (st[r] + k) % 8
        ed[r] = (ed[r] + k) % 8

ans = 0
for r in range(G):
    if gear[r][(st[r] - 2) % 8] == '1':
        ans += 2 ** r
print(ans)
