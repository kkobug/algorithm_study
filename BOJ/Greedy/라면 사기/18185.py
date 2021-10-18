"""
https://www.acmicpc.net/problem/18185
"""
def get_3(x):
    temp = min(ramen[x], ramen[x + 1], ramen[x + 2])
    if temp:
        ramen[x] -= temp
        ramen[x + 1] -= temp
        ramen[x + 2] -= temp
    return temp

N = int(input())
ramen = list(map(int, input().split()))
ans = 0

for i in range(N-2):
    if not ramen[i]:
        continue
    if ramen[i+1] > ramen[i+2]:
        temp = min(ramen[i], ramen[i+1]-ramen[i+2])
        ans += 5*temp
        ramen[i] -= temp
        ramen[i+1] -= temp

        temp = get_3(i)
        ans += 7*temp
    else:
        temp = get_3(i)
        ans += 7*temp
    if ramen[i]:
        ans += 3*ramen[i]
        ramen[i] = 0
temp = min(ramen[-1], ramen[-2])
ans += 5*temp
ramen[-1] -= temp
ramen[-2] -= temp
if ramen[-1]:
    ans += 3*ramen[-1]
if ramen[-2]:
    ans += 3*ramen[-2]

print(ans)