"""
N개의 정점과 M개의 간선으로 구성된 가중치가 없는 무방향 그래프에서의 최장 경로의 길이를 계산하자.
정점의 번호는 1번부터 N번까지 순서대로 부여되어 있다.
경로에는 같은 정점의 번호가 2번 이상 등장할 수 없으며, 경로 상의 인접한 점들 사이에는 반드시 두 정점을 연결하는 간선이 존재해야 한다.
경로의 길이는 경로 상에 등장하는 정점의 개수를 나타낸다.

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 두 개의 자연수 N M(1 ≤ N ≤ 10, 0 ≤ M ≤ 20)이 주어진다.
두 번째 줄부터 M개의 줄에 걸쳐서 그래프의 간선 정보를 나타내는 두 정수 x y(1 ≤ x, y ≤ N)이 주어진다.
x와 y는 서로 다른 정수이며, 두 정점 사이에 여러 간선이 존재할 수 있다.
[출력]
각 테스트 케이스마다 ‘#x ’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 그래프에서의 최장 경로의 길이를 출력한다.

입력
2
1 0
3 2
1 2
3 2
출력
#1 1
#2 3
"""
def dfs(idx, cnt=1):
    global ans
    if ans < cnt:
        ans = cnt

    for i in graph[idx]:  # 이번 정점의 인접 정점들 중에서
        if not V[i]:  # 방문하지 않은 곳이 있다면 탐색
            V[i] = True
            dfs(i, cnt+1)
            V[i] = False

for tc in range(int(input())):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):  # 인접 리스트로 그래프 만들기
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    V = [False] * (N+1)  # 방문체크

    ans = 0
    for k in range(1, N+1):
        V[k] = True  # 첫 번째 노드 체크하고 탐색 시작
        dfs(k)
        V[k] = False
    print(f'#{tc+1} {ans}')
