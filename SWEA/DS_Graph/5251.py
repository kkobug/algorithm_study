"""
A도시에는 E개의 일방통행 도로 구간이 있으며, 각 구간이 만나는 연결지점에는 0부터 N번까지의 번호가 붙어있다.
구간의 시작과 끝의 연결 지점 번호, 구간의 길이가 주어질 때
0번 지점에서 N번 지점까지 이동하는데 걸리는 최소한의 거리가 얼마인지 출력하는 프로그램을 만드시오.
모든 연결 지점을 거쳐가야 하는 것은 아니다.

[입력]
첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 첫 줄에 마지막 연결지점 번호N과 도로의 개수 E가 주어진다.
다음 줄부터 E개의 줄에 걸쳐 구간 시작 s, 구간의 끝 지점 e, 구간 거리 w가 차례로 주어진다. ( 1<=T<=50, 1<=N, s, e<=1000, 1<=w<=10, 1<=E<=1000000 )

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.

입력
3
2 3
0 1 1
0 2 6
1 2 1
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10
출력
#1 2
#2 4
#3 10
"""
#BFS
# from collections import deque
#
# for tc in range(int(input())):
#     N, E = map(int, input().split())
#     A = [[] for _ in range(N+1)]
#     dist = [10000]*(N+1)
#     for _ in range(E):
#         s, e, w = map(int, input().split())
#         A[s].append([e, w])
#
#     Q = deque([0])  # 시작하는 지점
#     dist[0] = 0
#     while Q:
#         now = Q.popleft()
#
#         for i in A[now]:  # 현재 정점으로부터 갈 수 있는 정점 돌면서
#             ed, w = i
#             d = dist[now] + w  # 다음 정점으로 가는 거리(= 지금까지 거리 + 다음 거리)
#             if d < dist[ed]:  # 갱신
#                 dist[ed] = d
#                 Q.append(ed)
#     print(f'#{tc+1} {dist[N]}')


# Dijkstra
for tc in range(int(input())):
    N, E = map(int, input().split())
    arr = [[] for _ in range(N+1)]
    dist = [0] + [999999999]*N
    visit = [False]*(N+1)
    for _ in range(E):
        st, ed, w = map(int, input().split())
        arr[st].append([ed, w])
        arr[ed].append([st, w])

    for _ in range(N):
        st = -1
        d = 999999999
        for i in range(N+1):
            if dist[i] < d and not visit[i]:
                st = i
                d = dist[i]

        visit[st] = True
        for next_st, next_d in arr[st]:
            if dist[st] + next_d < dist[next_st]:
                dist[next_st] = dist[st] + next_d

    print(f'#{tc+1} {dist[N]}')
