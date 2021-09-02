"""
def inorder(n):  # 중위순회
    if n:
        inorder(left[n])
        print(node[n - 1][1], end="")
        inorder(right[n])


for tc in range(1, 11):
    N = int(input())
    node = []
    tree = []
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    for _ in range(N):
        arr = list(input().split())
        node.append([int(arr.pop(0)), arr.pop(0)])  # node에는 input에 들어갈 알파벳을 저장하고
        if arr:
            while arr:
                tree.append(int(node[-1][0]))  # tree에는 연결되는 노드 번호를 저장
                tree.append(int(arr.pop(0)))

    for i in range(N - 1):
        p, c = tree[i * 2], tree[i * 2 + 1]  # 저장할 노드 위치 지정
        if left[p] == 0:  # 왼쪽 자식이 없으면 왼쪽에 저장하고
            left[p] = c
        else:  # 왼쪽 자식이 있으면 오른쪽에 저장
            right[p] = c
    print(f"#{tc}", end=" ")
    inorder(1)  # 중위순회
    print()
"""


def inorder(n):  # 중위순회
    if 2*n < N+1:  # 노드 연결을 받지 않았으므로 리스트 범위를 넘지 않도록 해야함
        inorder(2*n)
    print(tree[n], end="")
    if 2*n < N:  # 노드 연결을 받지 않았으므로 리스트 범위를 넘지 않도록 해야함
        inorder(2*n + 1)


for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)
    for i in range(N):  # 주어질 트리가 완전 이진트리임을 조건에 그림으로 나타냈으므로
        node = input().split()
        tree[int(node[0])] = node[1]  # 노드 번호와 해당 알파벳만을 tree에 저장한다 (어디로 가는지는 중요하지않음)

    print(f"#{tc}", end=" ")
    inorder(1)
    print()
