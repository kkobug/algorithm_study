"""
https://www.acmicpc.net/problem/20055
예제 입력 1
3 2
1 2 1 2 1 2
예제 출력 1
2
"""
from collections import deque

N, K = map(int, input().split())
belt = deque(map(int, input().split()))
robot = deque([False]*(2*N))
ans = 0

while belt.count(0) < K:
    ans += 1
    belt.rotate(1)
    robot.rotate(1)
    robot[N-1] = False

    for i in range(N-1, -1, -1):
        if robot[i] and not robot[i+1] and belt[i+1]:
            robot[i+1] = True
            robot[i] = False
            belt[i+1] -= 1
    robot[N-1] = False

    if belt[0] and not robot[0]:
        robot[0] = True
        belt[0] -= 1

print(ans)
