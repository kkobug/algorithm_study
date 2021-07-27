def max_numer():
    T = int(input())
    number_list = []
    result_cnt = 0

    for i in range(T):
        number_list.append(list(map(int, input().split())))
    
    for j in number_list:
        result = j[0]
        for k in j:
            if k >= result:
                result = k
        result_cnt += 1
        print(f'#{result_cnt} {result}')

max_numer()