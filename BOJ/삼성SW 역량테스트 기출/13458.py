# https://www.acmicpc.net/problem/13458
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
ans = 0

for i in range(N):
    A[i] -= B
    ans += 1

    if A[i] > 0:
        if A[i]%C:
            ans += 1
        ans += A[i]//C

print(ans)