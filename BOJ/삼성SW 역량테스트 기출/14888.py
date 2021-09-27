"""
https://www.acmicpc.net/problem/14888
예제 입력
6
1 2 3 4 5 6
2 1 1 1
예제 출력
54
-24
"""
def calculate(a, b, x):
    if x == 0:
        return a + b
    if x == 1:
        return a - b
    if x == 2:
        return a * b
    if x == 3:
        if a < 0:
            return -((-a)//b)
        else:
            return a//b


def push(num, op, idx=1):
    global ans_min, ans_max
    if idx == N:
        ans_min = min(ans_min, num)
        ans_max = max(ans_max, num)

    for i in range(4):
        if op[i]:
            op[i] -= 1
            push(calculate(num, nums[idx], i), op, idx+1)
            op[i] += 1


N = int(input())
nums = list(map(int, input().split()))
operator = list(map(int, input().split()))
ans_max = -1000000000
ans_min = 1000000000
push(nums[0], operator)
print(ans_max)
print(ans_min)