"""
https://www.acmicpc.net/problem/18186
"""
N, B, C = map(int, input().split())
ramen = list(map(int, input().split()))
ans = 0
D = B + C
T = B + 2*C

# B <= C 즉, 여러개 사는게 손해일 경우
if B <= C:
    ans += B*sum(ramen)
# B > C small과 같은 경우
else:
    for i in range(N-2):
        if not ramen[i]:
            continue
        if ramen[i+1] > ramen[i+2]:
            temp = min(ramen[i], ramen[i+1]-ramen[i+2])
            ans += D*temp
            ramen[i] -= temp
            ramen[i+1] -= temp

            temp = min(ramen[i], ramen[i+1], ramen[i+2])
            if temp:
                ans += T*temp
                ramen[i] -= temp
                ramen[i+1] -= temp
                ramen[i+2] -= temp
        else:
            temp = min(ramen[i], ramen[i+1], ramen[i+2])
            ans += T*temp
            ramen[i] -= temp
            ramen[i+1] -= temp
            ramen[i+2] -= temp
        if ramen[i]:
            ans += B*ramen[i]
            ramen[i] = 0
    temp = min(ramen[-1], ramen[-2])
    ans += D*temp
    ramen[-1] -= temp
    ramen[-2] -= temp
    if ramen[-1]:
        ans += B*ramen[-1]
    if ramen[-2]:
        ans += B*ramen[-2]

print(ans)