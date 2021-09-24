from pprint import pprint

def play(FOOD, shark, cnt=0):
    global ans
    if not FOOD:
        return

    if ans < cnt:
        ans = cnt
    move()
    s_temp = shark[:]
    for F in FOOD:
        # 방향, 좌표, 먹은 수
        shark[0] = aquarium[F[0]][F[1]][1]
        shark[1], shark[2] = F[0], F[1]
        shark[3] = aquarium[F[0]][F[1]][0]
        play(eat(), shark, cnt+shark[3])
        shark = s_temp[:]


def eat():
    food = []
    sr, sc = shark[1], shark[2]
    sd = shark[0]
    while True:
        nsr = sr + direction[sd][0]
        nsc = sc + direction[sd][1]
        if 0 <= nsr < 4 and 0 <= nsc < 4:
            if aquarium[nsr][nsc]:
                food.append((nsr, nsc))
            sr, sc = nsr, nsc
        else:
            break
    return food

def move():
    for i in range(1, 17):
        if not fish[i]:
            continue
        r, c = fish[i]
        d = aquarium[r][c][1]
        # f = aquarium[r][c][0]
        while True:
            nr = r + direction[d][0]
            nc = c + direction[d][1]
            if 0 <= nr < 4 and 0 <= nc < 4 and (nr, nc) != (shark[1], shark[2]):
                break
            else:
                d = (d+1) % 8
        if aquarium[nr][nc]:
            nf = aquarium[nr][nc][0]
            # nd = aquarium[nr][nc][1]
            # 이제 nr과 nc는 i번 물고기(=f)가 갈곳
            # r, c는 i번 물고기 좌표, nr, nc는 바뀔 좌표
            # nf랑 nd는 새 물고기랑 새 물고기 방향
            temp = aquarium[r][c][:]
            aquarium[r][c] = aquarium[nr][nc][:]
            aquarium[nr][nc] = temp[:]

            temp = fish[i][:]
            fish[i] = fish[nf][:]
            fish[nf] = temp[:]
        else:
            aquarium[nr][nc] = aquarium[r][c][:]
            aquarium[r][c] = []
            fish[i] = [nr, nc]



direction = [[-1, 0], [-1, -1], [0, -1],
             [1, -1], [1, 0], [1, 1],
             [0, 1], [-1, 1]]

# 물고기번호, 방향
aquarium = [[],
            [],
            [],
            []]
# i번 물고기 좌표
fish = [[] for _ in range(17)]
# 상어 정보(방향, 좌표, 먹은 수)
shark = [0, 0, 0, 0]

for i in range(4):
    inp = list(map(int, input().split()))
    for j in range(4):
        aquarium[i].append([inp[2*j]] + [inp[2*j+1]-1])
        fish[inp[2*j]] = [i, j]

# pprint(aquarium)
# pprint(fish)

shark[0] = aquarium[0][0].pop()
shark[1], shark[2] = fish[aquarium[0][0][0]]
shark[3] = aquarium[0][0].pop()

# pprint(shark)
# pprint(aquarium)

ans = 0
play(eat(), shark)

print(ans)