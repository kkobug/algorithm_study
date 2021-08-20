N, need = map(int, input().split())
catalogue = [list(map(int, input().split())) for _ in range(N)]
pipe = [0]*10001
for i in range(N):
    for j in range(1, catalogue[i][1]+1):
        pipe[j * catalogue[i][0]] = pipe[(j-1) * catalogue[i][0]] + 1

print(pipe[:22])
# print(pipe[need])