import inputcase

def divide(num_list):
    if len(num_list) <= 1:
        return num_list
    mid = len(num_list) // 2
    left = divide(num_list[:mid])
    right = divide(num_list[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

def average(num_list):
    result = []
    for num in num_list:
        sum_num = 0
        cnt_num = 0
        for i in divide(num)[1:-1]:
            sum_num += i
            cnt_num += 1
        result.append(int(round(sum_num/cnt_num)))
    return result

input_list = inputcase.input_list_return_list()
result = average(input_list)
inputcase.output(result)