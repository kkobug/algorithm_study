"""
V, E, 간선정보가 주어질 때 최소 신장 트리 (모든 정점을 방문할 때, 가장 작은 간선들을 선택하는 경우)
정점을 기준으로 선택해 나가면서 다음 정점까지의 거리정보를 최신화 해나가는 방법
모든 정점을 기준으로 갈 수 있는 정점들을 탐색해야 하므로 O(V^2)

예시 코드는 가장 큰 정점이 V번, 간선의 수가 E개인 그래프에 대한 MST에서 간선크기의 총합을 계산
ex input...
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
ex output...
175
"""
V, E = map(int, input().split())
arr = [[] for _ in range(V+1)]
for _ in range(E):
    st, ed, w = map(int, input().split())
    arr[st].append([ed, w])  # 양뱡향 그래프일 경우에 대한 코드
    arr[ed].append([st, w])

dist = [0] + [9999]*V  # 그래프의 가중치로 나올 수 있는 결과보다 큰 값을 거리(dist) 리스트에 저장
visit = [False]*(V+1)  # 시작 정점(0번으로 가정)에서 거리는 0으로 두고 시작

for _ in range(V):  # 정점의 개수가 V+1개 이므로 V번만큼 정점을 선택해야함
    st = -1
    d = 9999
    for i in range(V+1):
        if dist[i] < d and not visit[i]:  # 갈 수 있는 정점 중에서, 가장 짧은 간선을 가진 것 선택
            st = i
            d = dist[i]

    visit[st] = True
    for next_st, next_d in arr[st]:  # 선택된 정점으로부터 갈 수 있는 거리들을 갱신
        if next_d < dist[next_st]:  # 다음 정점까지 거리가 지금 선택한 것 보다 길고
            if not visit[next_st]:  # 그 정점이 아직 안가본 곳이라면
                dist[next_st] = next_d

print(sum(dist))