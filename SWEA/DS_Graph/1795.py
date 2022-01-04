"""
※ SW Expert 아카데미의 문제를 무단 복제하는 것을 금지합니다.
인수가 사는 마을에는 N개의 집이 있고, 각 집에는 한 명의 사람이 살고 있다.
N개의 집을 정점으로 볼 때, 도로는 어떤 집에서 다른 어떤 집으로 이동이 가능한 단방향 간선으로 볼 수 있다.
도로는 모든 집들 간에 이동이 가능하도록 구성되어 있다.
집에 1번에서 N번까지의 번호를 붙일 때, 인수의 집은 X번 집이다.
오늘은 인수의 생일이기 때문에 모든 마을 사람들이 인수의 생일을 축하해주기 위해 X번 집으로 모인다.
각 사람들은 자신의 집에서 X번 집으로 오고 가기 위해 최단 시간으로 이동한다.
도로가 단 방향이기 때문에 이용하는 도로는 오고 갈 때 다를 것이다.

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 세 정수 N,M,X(1 ≤ X ≤ N ≤ 1,000, 1 ≤ M ≤ 10,000)가 공백으로 구분되어 주어진다.
다음 M개의 각 줄에는 세 정수 x, y, c (1 ≤ x, y ＜ N, 1 ≤ c ≤ 100)가 공백으로 구분되어 주어진다.
이는 x번 집에서 y번 집으로 가는 데 시간이 c가 걸리는 단 방향 도로가 존재한다는 뜻이다.

[출력]
각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
오고 가는데 걸리는 시간이 가장 긴 거리를 출력한다.

입력
1
4 8 2
1 2 4
1 3 2
1 4 7
2 1 1
2 3 5
3 1 2
3 4 4
4 2 3

출력
#1 10
"""
for tc in range(int(input())):
    N, M, X = map(int, input().split())
    go_arr = [[] for _ in range(N+1)]
    back_arr = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        go_arr[x].append([y, c])
        back_arr[y].append([x, c])

    go_dist = [float('inf')] * (N+1)
    back_dist = [float('inf')] * (N+1)
    go_dist[X] = back_dist[X] = 0
    go_visit = [False] * (N+1)
    back_visit = [False] * (N+1)

    for _ in range(N):
        go_st = -1
        go_val = float('inf')
        back_st = -1
        back_val = float('inf')
        for i in range(1, 1+N):
            if go_dist[i] < go_val and not go_visit[i]:
                go_st = i
                go_val = go_dist[i]
            if back_dist[i] < back_val and not back_visit[i]:
                back_st = i
                back_val = back_dist[i]

        go_visit[go_st] = back_visit[back_st] = True
        for ed, next_val in go_arr[go_st]:
            if go_dist[go_st] + next_val < go_dist[ed]:
                go_dist[ed] = go_dist[go_st] + next_val
        for ed, next_val in back_arr[back_st]:
            if back_dist[back_st] + next_val < back_dist[ed]:
                back_dist[ed] = back_dist[back_st] + next_val

    ans = 0
    for i in range(1, 1+N):
        ans = max(ans, go_dist[i]+back_dist[i])
    print(f'#{tc+1} {ans}')