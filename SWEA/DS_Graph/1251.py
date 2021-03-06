"""
N개의 섬들을 연결하는 교통시스템 설계 프로젝트인 ‘하나로’를 진행하게 되었습니다.
모든 섬을 해저터널로 연결하는 것을 목표로 합니다.
해저터널은 반드시 두 섬을 선분으로 연결하며, 두 해저 터널이 교차된다 하더라도 물리적으로는 연결되지 않는 것으로 가정합니다.
해저터널 건설로 인해 파괴되는 자연을 위해 다음과 같은 환경 부담금 정책이 있습니다.

- 환경 부담 세율(E)과 각 해저터널 길이(L)의 제곱의 곱(E * L2)만큼 지불
총 환경 부담금을 최소로 지불하며, N개의 모든 섬을 연결할 수 있는 교통 시스템을 설계하시오.
64비트 integer 및 double로 처리하지 않을 경우, overflow가 발생할 수 있습니다 (C/C++ 에서 64비트 integer는 long long 으로 선언).

[입력]
가장 첫 줄은 전체 테스트 케이스의 수이다.
각 테스트 케이스의 첫 줄에는 섬의 개수 N이 주어지고 (1≤N≤1,000),
두 번째 줄에는 각 섬들의 정수인 X좌표, 세 번째 줄에는 각 섬들의 정수인 Y좌표가 주어진다 (0≤X≤1,000,000, 0≤Y≤1,000,000).
마지막으로, 해저터널 건설의 환경 부담 세율 실수 E가 주어진다 (0≤E≤1).
[출력]
각 테스트 케이스의 답을 순서대로 출력하며, 각 케이스마다 줄의 시작에 “#C”를 출력하여야 한다. 이때 C는 케이스의 번호이다.
같은 줄에 빈칸을 하나 두고, 주어진 입력에서 모든 섬들을 잇는 최소 환경 부담금을 소수 첫째 자리에서 반올림하여 정수 형태로 출력하라.

입력
10
2
0 0
0 100
1.0
4
0 0 400 400
0 100 0 100
1.0
6
0 0 400 400 1000 2000
0 100 0 100 600 2000
0.3
9
567 5 45674 24 797 29 0 0 0
345352 5464 145346 54764 5875 0 3453 4545 123
0.0005
출력
#1 10000
#2 180000
#3 1125000
#4 27365366
"""
# prim
for tc in range(int(input())):
    N = int(input())
    island = [[] for _ in range(N)]
    for _ in range(2):
        temp = list(map(int, input().split()))
        for d in range(N):
            island[d].append(temp[d])
    E = float(input())

    dist = [0.0] + [float('inf')]*(N-1)
    visit = [False]*N

    for _ in range(N):
        st = -1
        d = float('inf')
        for i in range(N):
            if dist[i] < d and not visit[i]:
                st = i
                d = dist[i]

        visit[st] = True
        i, j = island[st]
        for k in range(N):
            ni, nj = island[k]
            nd = E * ((ni-i)**2 + (nj-j)**2)
            if not visit[k] and nd < dist[k]:
                dist[k] = nd
    print(f'#{tc+1} {round(sum(dist))}')
