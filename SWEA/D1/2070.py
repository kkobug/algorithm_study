def large_small_same():
    T = int(input())
    number_list = []
    result_cnt = 0

    for i in range(T):
        number_list.append(list(map(int, input().split())))
    
    for number in number_list:
        if number[0] > number[1]:
            result = '>'
        elif number[0] < number[1]:
            result = '<'
        else:
            result = '='
        result_cnt += 1
        print(f'#{result_cnt} {result}')

large_small_same()