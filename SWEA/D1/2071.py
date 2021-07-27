def get_avg():
    T = int(input())
    number_list = []
    result_cnt = 0

    for i in range(T):
        number_list.append(list(map(int,input().split())))
        
    for i in number_list:
        result_sum = 0
        result_num = 0
        for j in i:
            result_sum += j
            result_num += 1
        result_cnt += 1
        print(f'#{result_cnt} {result_sum/result_num:.0f}')

get_avg()