# 조합
def combi():
    for tc in range(1, 1+int(input())):
        N = int(input())//10
        f = [1]*(N+1)
        ans = 0
        for i in range(2, N+1):  # 조합을 위한 factorial memo
            f[i] = i*f[i-1]
        for x in range(N%2, N+1, 2):
            y = (N-x)//2
            ans += (2**y)*f[x+y]//(f[x]*f[y])  # 조합식
        print("#{} {}".format(tc, ans))


combi()

"""
# 점화식
def recur():
    for tc in range(1, 1+int(input())):
        N = int(input())//10
        ans = [0, 1, 3] + [0]*(N-2)
        for i in range(3, N+1):
            ans[i] = ans[i-1] + 2*ans[i-2]
        print("#{} {}".format(tc, ans[N]))


recur()
"""