class Heap():

    def __init__(self):
        self.heap = [0]


class MinHeap(Heap):

    def node(self, i):
        return self.heap[i]

    def push(self, i):
        self.heap.append(i)  # n번째 데이터가 들어가면, 리스트 길이는 n+1이므로
        point = len(self.heap) - 1  # 데이터의 위치는 n이 되어야 함

        while point > 1:  # 루트노드가 아니라면
            if self.heap[point] < self.heap[point//2]:  # 부모노드가 더 클 경우
                self.heap[point//2], self.heap[point] = self.heap[point], self.heap[point//2]
                point //= 2
            else:
                break  # 자식노드가 더 커지면 (최소힙 성립)

    def delete(self):
        self.heap[1] = self.heap.pop()
        point = 1
        length = len(self.heap) - 1
        while 2*point+1 <= length:
            lc = 2*point
            rc = 2*point+1
            c = lc
            if self.heap[rc] < self.heap[lc]:  # 자식노드 중 값이 작은 노드를 고르기
                c = rc

            if self.heap[c] < self.heap[point]:  # 작은 노드보다 더 부모노드가 더 크면 바꾸기
                self.heap[point], self.heap[c] = self.heap[c], self.heap[point]
            else:
                return
            point = c

        if 2*point == length:  # 자식노드가 하나남은 경우 처리
            if self.heap[2*point] < self.heap[point]:
                self.heap[2*point], self.heap[point] = self.heap[point], self.heap[2*point]
        return

    def __str__(self):
        return str(self.heap)


for tc in range(1, 1+int(input())):
    N = int(input())
    nums = list(map(int, input().split()))
    tree = MinHeap()

    for n in nums:
        tree.push(n)

    ans = 0
    while N > 0:
        N //= 2
        ans += tree.node(N)

    print(f'#{tc} {ans}')
    print(tree)
    tree.delete()
    print(tree)
