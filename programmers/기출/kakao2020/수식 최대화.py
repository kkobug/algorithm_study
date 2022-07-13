"""
https://school.programmers.co.kr/learn/courses/30/lessons/67257
"""
def get_order(expression_order):
    global answer, operator_list, expression_list
    if len(expression_order) == 3:
        value = calculate(calculate(
                calculate(expression_list, operator_list[expression_order[0]])
                , operator_list[expression_order[1]]), operator_list[expression_order[2]])[0]
        value = value if value >= 0 else -value
        answer = answer if answer >= value else value
        return

    for i in range(3):
        if i in expression_order:
            continue
        expression_order.append(i)
        get_order(expression_order)
        expression_order.pop()


def get_value(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    else:
        return a * b


def calculate(expression, operator):
    new_expression_list = []
    for e in expression:
        if new_expression_list and new_expression_list[-1] == operator:
            temp_op = new_expression_list.pop()
            temp_num = new_expression_list.pop()
            new_expression_list.append(get_value(temp_num, e, temp_op))
        else:
            new_expression_list.append(e)
    return new_expression_list


def solution(expression):
    global answer, expression_list, operator_list
    operator_list = ["+", "*", "-"]
    answer = 0
    expression_list = []
    temp = ""
    for e in expression:
        if "0" <= e <= "9":
            temp += e
        else:
            expression_list.append(int(temp))
            expression_list.append(e)
            temp = ""
    else:
        expression_list.append(int(temp))

    get_order([])
    return answer


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
