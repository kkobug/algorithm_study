"""
https://www.acmicpc.net/problem/1931
예제 입력 1
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
예제 출력 1
4
"""
N = int(input())
meet = [list(map(int, input().split())) for _ in range(N)]
meet.sort(key=lambda x:(x[1], x[0]))
ans = 1
k = meet[0][1]
for i in range(1, N):
    if k <= meet[i][0]:
        k = meet[i][1]
        ans += 1

print(ans)
