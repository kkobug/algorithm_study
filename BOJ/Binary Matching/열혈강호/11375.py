from sys import stdin
input = stdin.readline


def match(k):
    if visit[k]:
        return
    visit[k] = True
    for j in worker[k]:
        if not work[j] or (k != work[j] and match(work[j])):
            work[j] = k
            return True
    return


N, M = map(int, input().split())
work = [0] * (M+1)
worker = [[]]
for _ in range(N):
    worker.append(list(map(int, input().split()))[1:])

ans = 0
for i in range(1, 1+N):
    visit = [False] * (N+1)
    if match(i):
        ans += 1

print(ans)
