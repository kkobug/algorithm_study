N = int(input())
drink = list(map(int, input().split()))
m, s = 0, 0
for i in range(N):
    if drink[i] > m:
        m = drink[i]
    s += drink[i]

print((s+m)/2)