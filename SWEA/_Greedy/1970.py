money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for tc in range(int(input())):
    print(f'#{tc+1}')
    N = int(input())
    ans = [0]*8
    for i in range(8):
        while N >= money[i]:
            ans[i] += 1
            N -= money[i]
    print(*ans)
