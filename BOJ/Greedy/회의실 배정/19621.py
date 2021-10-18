N = int(input())
room = [list(map(int, input().split())) for _ in range(N)]
room.sort(key=lambda x:(x[1], x[0], -x[2]))
print(room)