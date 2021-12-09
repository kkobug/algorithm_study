"""
https://www.acmicpc.net/problem/16637
"""
def calculate(x, y, op):
    if op == "+":
        return x + y
    if op == "*":
        return x * y
    if op == "-":
        return x - y


def dfs(idx=0, operator="+", cnt=0):
    global ans
    if N <= idx:
        ans = max(ans, cnt)
        return

    if idx == N-1:
        dfs(idx+2, "+", calculate(cnt, expression[idx], operator))
    elif idx < N-1:
        dfs(idx+2, expression[idx+1], calculate(cnt, expression[idx], operator))

    if idx == N-3:
        dfs(idx+4, "+", calculate(cnt, calculate(expression[idx], expression[idx+2], expression[idx+1]), operator))
    elif idx < N-3:
        dfs(idx+4, expression[idx+3], calculate(cnt, calculate(expression[idx], expression[idx+2], expression[idx+1]), operator))


N = int(input())
ans = -float('inf')
expression = list(input())
for e in range(N):
    try:
        expression[e] = int(expression[e])
    except:
        continue
dfs()
print(ans)
