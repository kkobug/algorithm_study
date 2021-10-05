for tc in range(1, 1+int(input())):
    N = int(input())
    dots = list(map(int, input().split()))
    ans = []
    for i in range(N-1):
        k = (dots[i+N+1]/dots[i+N]) ** 0.5
        ans.append((k*dots[i] + dots[i+1])/(k+1))
    print(*ans)