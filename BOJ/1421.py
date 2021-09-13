"""
https://www.acmicpc.net/problem/1421
예제 입력 1
3 1 10
26
103
59
예제 출력 1
1770
"""
N, C, W = map(int, input().split())
woods = [int(input()) for _ in range(N)]
ans = 0
for i in range(1, max(woods)+1):
    temp = 0
    for wood in woods:
        if wood < i:
            continue
        temp += W*(wood//i) * i
        if wood%i:
            temp -= C*(wood//i)
        else:
            temp -= C*(wood//i - 1)

    if temp > ans:
        ans = temp

print(ans)
