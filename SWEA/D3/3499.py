def shuffle(cards, N):
    ans =[]
    mid = (N+1)//2
    left = cards[:mid]
    right = cards[mid:]

    for m in range(len(right)):
        ans.append(left[m])
        ans.append(right[m])

    if N%2:
        ans.append(left[-1])

    return ans


for tc in range(1, 1+int(input())):
    N = int(input())
    c = input().split()
    print(f"#{tc}", end=" ")
    print(*shuffle(c, N))
