"""
기지국의 위치와 집들이 표시된 지도를 2차원 NxN 배열로 변환하여
기지국에 커버되지 않는 집의 수를 찾고자한다. X는 빈칸, H는 집을 나타낸다.
기지국은 A, B, C 세 종류가 있다.
각각의 기지국은 기지국이 위치한 셀에서 동서남북으로 A: 1, B: 2, C: 3개의 셀을 커버한다.
즉, 각 기지국은 십자가모양으로 A는 5칸, B는 9칸, C는 13칸을 커버할 수 있다.
이때, 기지국에 커버되지 않는 집의 수를 출력하는 프로그램을 작성하시오.

첫째줄에는 테스트 케이스 수를 입력받는다.
둘째줄에는 도시의 크기 N을 입력받는다.
셋째줄부터는 집과 기지국을 나타내는 입력을 N개 받는다.

sol
돌면서 A, B, C의 위치를 받아놓는다
각 위치마다 델타변환을 통해 집을 X로 바꾼다
남은 집의 수를 센다

입력
2
9
XXXXXXXXX
XXXHXXXXX
XXHAHXXHX
XXHHXXXXX
XXXXXXXXX
XXAHHXXXX
XXHXXHAHX
XXAHXXHXX
XXHXHXXXX
12
XXXHXXXXXXXA
XXXHXXXXXXXX
XXHHHXXXXXXX
XXXBHHXXXAXX
XXXXXXXHXHXX
XXXHXXHXXXXX
XXXXXXXXXXXX
XXXXHXXHXXXX
XXXXXXXCHXXH
XXHXXXHHXXXX
XXXXXXXXXXXX
BHXXXXXHXXXX

출력
#1 4
#2 9
"""
for tc in range(1, 1+int(input())):
    N = int(input())
    station = [[], [], []]
    city, di, dj = [], [], []
    ans = 0
    for i in range(N):
        city.append(list(input()))
        for j in range(N):
            if city[i][j] == 'A':
                station[0].append((i, j))
            elif city[i][j] == 'B':
                station[1].append((i, j))
            elif city[i][j] == 'C':
                station[2].append((i, j))

    for t in range(3):
        di.extend([t+1, -t-1, 0, 0])
        dj.extend([0, 0, t+1, -t-1])

        while station[t]:
            i, j = station[t].pop()

            for d in range(len(di)):
                ni = i + di[d]
                nj = j + dj[d]
                if 0 <= ni < N and 0 <= nj < N and city[ni][nj] == 'H':
                    city[ni][nj] = 'X'

    for x in city:
        ans += x.count('H')

    print("#{} {}".format(tc, ans))
