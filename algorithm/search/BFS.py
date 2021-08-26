"""
너비 우선 탐색(Breadth First Search)에 대한 코드
그래프를 탐색할 때, 인접 정점들을 탐색한 후 찾은 인접 정점들을 시작접으로 인접 정점을 탐색하는 방법

"""

# ex
# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7


def bfs(s, V):
    q = [0] * V             # 큐 생성
    front = rear = -1
    visited = [0] * (V+1)   # visited 생성
    rear += 1               # 시작점 인큐
    q[rear] = s             # 시작점 방문
    visited[s] = 1          # 시작점 방문 체크

    while front != rear:    # 큐가 비어있찌 않으면
        front += 1          # dequeue
        t = q[front]        # dequeue 값 t에 저장
        for i in range(1, V+1):  # t에 인접하고 방문하지 않은 모든 i에 대해
            if adj[t][i] and not visited[i]:    # enqueue
                rear += 1
                q[rear] = 1
                visited[i] = visited[t] + 1     # 방문 체크???


V, E = map(int, input().split())
edge = list(map(int, input().split()))
adj = [[0]*(V+1) for _ in range(V+1)]
adj_list = [[] for _ in range(V+1)]