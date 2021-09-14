"""
https://www.acmicpc.net/problem/1531
예제 입력 1
3 1
21 21 80 80
41 41 60 60
71 71 90 90
예제 출력 1
500
"""
N, M = map(int, input().split())
picture = [[M]*100 for _ in range(100)]

for _ in range(N):
    si, sj, ei, ej = map(int, input().split())
    for i in range(si-1, ei):
        for j in range(sj-1, ej):
            picture[i][j] -= 1

ans = 0
for i in range(100):
    for j in range(100):
        if picture[i][j] < 0:
            ans += 1

print(ans)