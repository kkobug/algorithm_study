N, M = map(int, input().split())
box = [list(map(int, input())) for _ in range(N)]
m = 0
if N > M: N, M = M, N
for s in range(1, N):
    for i in range(N-s+1):
        for j in range(M-s+1):
            if box[i][j] == box[i][j+s-1] == box[i+s-1][j] == box[i+s-1][j+s-1]:
                if s > m: m = s
print((s+1)*(s+1))