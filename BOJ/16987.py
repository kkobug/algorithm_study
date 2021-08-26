from sys import stdin as st


def attack(a, b):
    a[0] -= b[1]
    b[0] -= a[1]


def heal(a, b):
    a[0] += b[1]
    b[0] += a[1]


def breaker(i=0):
    global ans

    if i == N:
        temp = 0
        for x in range(N):
            if eggs[x][0] <= 0:
                temp += 1
        if ans < temp:
            ans = temp
        return

    if eggs[i][0] <= 0:
        breaker(i+1)
        return

    for egg in range(N):
        if egg == i:
            pass
        elif eggs[egg][0] > 0:
            attack(eggs[i], eggs[egg])
            breaker(i+1)
            heal(eggs[i], eggs[egg])
    else:
        breaker(i+1)


N = int(st.readline())
ans = 0
eggs = [list(map(int, st.readline().split())) for _ in range(N)]
# eggs[i][0] = 체력, eggs[i][1] = 공격력
breaker()
print(ans)
