"""
1. 모든 간선을 가중치에 따라 오름차순 정렬
2. 가중치가 낮은 간선부터 선택하고, 사이클이 되면 선택하지않음
3. n-1개의 간선이 선택되면 종료

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


def find_set(x):
    if P[x] != x:
        P[x] = find_set(P[x])
    return P[x]


V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
edges.sort(reverse=True, key=lambda x: x[2])  # sort for KRUSKAL
P = list(range(V+1))  # make_set
ans = cnt = 0
while cnt < V:
    st, ed, w = edges.pop()
    if find_set(st) == find_set(ed):
        continue
    P[find_set(ed)] = find_set(st)  # union
    ans += w
    cnt += 1
print(ans)
