def sum_odd():
    T = int(input())
    number_list = []
    result_cnt = 0

    for i in range(T):
        number_list.append(list(map(int,input().split())))
        
    for i in number_list:
        result_sum = 0
        for j in i:
            if j%2:
                result_sum += j
        result_cnt += 1
        print(f'#{result_cnt} {result_sum}')

sum_odd()