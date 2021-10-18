from sys import stdin
input = stdin.readline

N = int(input())
room = [list(map(int, input().split())) for _ in range(N)]
room.sort(key=lambda x: x[1])

k = room[0][1]
cnt = room[0][2]
for i in range(1, N):
    if k <= room[i][0]:
        k = room[i][1]
        cnt += room[i][2]

print(cnt)