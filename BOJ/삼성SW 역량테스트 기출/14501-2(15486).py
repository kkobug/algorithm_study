"""
퇴사2
https://www.acmicpc.net/problem/15486
"""
from sys import stdin as st

N = int(st.readline())
date = [list(map(int, st.readline().split())) for _ in range(N)]
ans = [0] * (N+1)

# # 앞에서부터 풀기
# for i in range(N):
#     if i + date[i][0] <= N:
#         ans[i+date[i][0]] = max(ans[i+date[i][0]], ans[i]+date[i][1])
#     ans[i+1] = max(ans[i+1], ans[i])
#
# print(ans[N])

# 뒤에서부터 풀기
for i in range(N-1, -1, -1):
    if i + date[i][0] > N:
        if i == N-1:
            ans[i] = 0
        else:
            ans[i] = ans[i+1]
    elif i + date[i][0] < N:
        if i == N-1:
            ans[i] = date[i][1]
        else:
            ans[i] = max(ans[i+1], date[i][1]+ans[i + date[i][0]])
    else:
        if i == N-1:
            ans[i] = date[i][1]
        else:
            ans[i] = max(ans[i+1], date[i][1])

print(ans[0])