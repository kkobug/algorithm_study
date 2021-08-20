N, M = map(int, input().split())
cards = list(map(int, input().split()))

ans = 0
l = len(cards)
for i in range(l-2):
    for j in range(i+1, l-1):
        for k in range(j+1, l):
            temp = sum([cards[i], cards[j], cards[k]])
            if ans < temp <= M:
                ans = temp

print(ans)