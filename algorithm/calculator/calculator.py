"""
수식을 받아 계산하는 계산기 만들기
- 중위표기를 받아 후위표기에 따라 계산한다

1. 입력 받은 중위 표기식에서 토큰을 읽는다
2. 토큰이 피연산자이면 토큰을 출력한다
3. 토큰이 연산자(괄호 포함)일때, 이 토큰이 스택의 top에 저장되어 있는 연산자보다 우선순위가 높으면 스택에 push하고,
 그렇지 않다면 스택 top의 연산자의 우선순위가 토큰의 우선순위보다 작을 때까지 스택에서 po한 후 토큰의 연산자를 push.
  만약 top에 연산자가 없으면 push
4. 포큰이 닫는 괄호이면 스택 top에 여는 괄호가 올때까지 스택에 pop을 수행하고 pop한 연산자를 출력한다.
 여는 괄호를 만나면 pop하고 출력하지는 않는다
5. 중위 표기식에 더 읽을 것이 없다면 중지하고, 읽을 것이 있다면 1부터 다시 반복
6. 스택에 남은 연산자를 모두 pop하여 출력: 스택 밖의 왼쪽 괄호는 우선 순위가 가장 높으며,
 스택 안의 왼쪽 괄호는 우선 순위가 가장 낮다.
"""

for tc in range(1, 11):
    N = int(input())
    infix = input()
    stack = []
    postfix = []

    op = {"*": 2, "/": 2, "+": 1, "-": 1, "(": 0}

    for inf in infix:
        if inf in "0123456789":  # 숫자는 그냥 출력
            postfix += inf
            continue

        if inf == ")":  # 닫는 괄호는 여는 괄호가 나올 때 까지 pop
            while stack[-1] != "(":
                postfix += stack.pop()
            stack.pop()

        elif stack and op[inf] <= op[stack[-1]]:  # 스택이 있는데 top 보다 우선순위가 낮다면
            while stack and op[inf] <= op[stack[-1]]:  # 그렇지 않을때까지 pop
                postfix += stack.pop()
            stack.append(inf)

        else:  # 스택이 비었거나, 우선순위가 높은 연산자면 그냥 push
            stack.append(inf)

    while stack:
        postfix += stack.pop()

    for pof in postfix:
        if pof in "0123456789":  # 숫자는 그냥 push
            stack.append(pof)
            continue

        else:  # -, / 연산은 순서가 상관없으므로 역순으로 연산
            temp_b = int(stack.pop())
            temp_a = int(stack.pop())
            if pof == "+":
                stack.append(temp_a + temp_b)
            elif pof == "*":
                stack.append(temp_a * temp_b)
            elif pof == "-":
                stack.append(temp_a - temp_b)
            elif pof == "/":
                stack.append(temp_a / temp_b)

    print("#{} {}".format(tc, stack.pop()))
