"""
문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오.
예를 들어
“3+4+5*6+7”
라는 문자열로 된 계산식을 후위 표기식으로 바꾸면 다음과 같다.
"34+56*+7+"
변환된 식을 계산하면 44를 얻을 수 있다.
문자열 계산식을 구성하는 연산자는 +, * 두 종류이며 피연산자인 숫자는 0 ~ 9의 정수만 주어진다.

[입력]
각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 길이가 주어진다. 그 다음 줄에 바로 테스트 케이스가 주어진다.
총 10개의 테스트 케이스가 주어진다.

[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 답을 출력한다.
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
