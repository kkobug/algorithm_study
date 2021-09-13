N, M = map(int, input().split())
cow = [list(map(int, input().split())) for _ in range(N)]
cow.sort(reverse=True)
home = [False] * (M + 1)
ans = 0
print(ans)