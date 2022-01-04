"""
※ SW Expert 아카데미의 문제를 무단 복제하는 것을 금지합니다.
그래프에서 사이클을 제거하고 모든 노드를 포함하는 트리를 구성할 때,
가중치의 합이 최소가 되도록 만든 경우를 최소신장트리라고 한다.
0번부터 V번까지의 노드와 E개의 간선을 가진 그래프 정보가 주어질 때,
이 그래프로부터 최소신장트리를 구성하는 간선의 가중치를 모두 더해 출력하는 프로그램을 만드시오.

[입력]
첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 첫 줄에 마지막 노드번호 V와 간선의 개수 E가 주어진다.
다음 줄부터 E개의 줄에 걸쳐 간선의 양 끝 노드 n1, n2, 가중치 w가 차례로 주어진다.
1<=T<=50, 1<=V<=1000, 1<=w<=10, 1<=E<=1000000

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

입력
1
2 3
0 1 1
0 2 1
1 2 6
출력
#1 2
"""
def find_set(x):
    if P[x] != x:
        P[x] = find_set(P[x])
    return P[x]

for tc in range(int(input())):
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
    print(f'#{tc+1} {ans}')
