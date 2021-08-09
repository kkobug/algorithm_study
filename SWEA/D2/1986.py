import inputcase

def odd_even(num_list):
    num_result = []
    cnt = 0
    for num in num_list:
        cnt += 1
        result = 0
        for n in range(1, num+1):
            if n % 2:
                result += n
            else:
                result -= n
        num_result.append(result)
    return num_result

input_num = inputcase.input_num_return_list()
inputcase.output(odd_even(input_num))


