def make_1(n):
    for i in range(n+1):
        ans[i] = ans[i]

N = int(input())
ans = [0, 0, 1, 1, 2] + [0]*N

