"""
https://www.acmicpc.net/problem/5430
"""
from collections import deque

for _ in range(int(input())):
    command = input()
    n = int(input())
    arr = input().split(',')
    arr[0] = arr[0][1:]
    arr[-1] = arr[-1][:len(arr[-1])-1]
    if arr == ['']:
        arr = deque()
    else:
        arr = deque(arr)

    try:
        direction = 0
        for c in command:
            if c == 'R':
                direction = 1 - direction
            else:
                if direction:
                    arr.pop()
                else:
                    arr.popleft()
        if direction:
            arr.reverse()
        arr = ','.join(arr)
        print('[' + arr + ']')
    except:
        print('error')
