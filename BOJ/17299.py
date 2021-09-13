N = int(input())
A = list(map(int, input().split()))
NGF = [0] * N
F = [[] for _ in range(max(A)+1)]

for i in range(N):
    F[A[i]].append(A[i])

print(F)
for i in range(N):
    for j in range(i+1, N):
        if F[j] > F[i]:
            NGF[i] += 1
    if NGF[i] == 0:
        NGF[i] = -1

print(*NGF)