from sys import stdin as st

N, x = map(int, st.readline().split())
pipe = [list(map(int, st.readline().split())) for _ in range(N)]
ans = [0] * (x+1)

max_data = 0
for j in range(N):
    max_data += (pipe[j][0] * pipe[j][1])
    ans[pipe[j][0]] += 1
    for k in range(pipe[j][0]+1, x+1):
        if k > max_data: break
        if ans[k] or ans[k - pipe[j][0]]:
            ans[k] += ans[k - pipe[j][0]]
            if k >= pipe[j][0] * (pipe[j][1] + 1):
                ans[k] -= (k-pipe[j][0]*pipe[j][1])//pipe[j][0]

print(ans)
print(ans[x])
