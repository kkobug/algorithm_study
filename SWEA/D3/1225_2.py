class CircularQueue:
    """
    처음 Circular Queue 문제를 풀기 전, 직접 Circular Queue 구현해보기
    """

    def __init__(self, items):
        self.queue = items
        self.len = len(items)
        self.front = 0
        self.rear = len(items) - 1

    def enqueue(self, data):
        self.rear = (self.rear + 1) % self.len
        self.queue[self.rear] = data

    def dequeue(self):
        self.front = (self.front + 1) % self.len
        return self.queue[self.front]

    def qpeek(self):
        return self.queue[(self.front + 1) % self.len]

    def __getitem__(self, index):
        return self.queue[index]

    def __setitem__(self, key, value):
        self.queue[key] = value

    def printq(self):  # 원형 큐는 공백이 존재하므로, 공백을 제외하고 front 뒤부터 rear까지 출력
        if self.front == 0: print(*self.queue[1:])
        elif self.front == self.len-1: print(*self.queue[:self.len-1])
        else: print(*self.queue[(self.front+1) % self.len:], *self.queue[:(self.rear+1) % nums.len])


for _ in range(10):
    print(f'#{input()}', end=" ")
    nums = CircularQueue([0] + list(map(int, input().split())))
    cnt = 0

    while nums[nums.rear] > 0:
        if nums.qpeek() - (cnt%5 + 1) < 0:          # Qpeek을 통해 감소할 때 0보다 작아지는지 검사
            nums[(nums.front + 1) % nums.len] = 0
        else:
            nums[(nums.front + 1) % nums.len] -= (cnt%5 + 1)
        cnt += 1

        nums.enqueue(nums.qpeek())                  # enqueue: 맨앞 값을 맨뒤로 넣기
        nums.dequeue()                              # dequeue

    nums.printq()
