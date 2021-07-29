def isdate():
    # 달력문제. 연월일 입력받아 가능성 판별하기
    T = int(input())
    number_list = []
    result_cnt = 0
    month_31 = ['01', '03', '05', '07', '08', '10', '12']
    month_30 = ['04', '06', '09', '11']
    month_special = ['02']
    month_list = [month_31, 31, month_30, 30, month_special, 28]

    for i in range(T):
        number_list.append(''.join(input()))

    for n in number_list:
        result = ''
        if len(n) == 8:
            if n[4:6] in month_31:     #일자를 int vs range로 표현할수있음
                if '01' <= n[6:] <= '31':
                    result = f'{n[:4]}/{n[4:6]}/{n[6:]}'
                else:
                    result = -1

            elif n[4:6] in month_30:
                if '01' <= n[6:] <= '30':
                    result = f'{n[:4]}/{n[4:6]}/{n[6:]}'
                else:
                    result = -1

            elif n[4:6] in month_special:
                if '01' <= n[6:] <= '28':
                    result = f'{n[:4]}/{n[4:6]}/{n[6:]}'
                else:
                    result = -1

            else:
                result = -1
        else:
            result = -1
        result_cnt += 1
        print(f'#{result_cnt} {result}')

isdate()