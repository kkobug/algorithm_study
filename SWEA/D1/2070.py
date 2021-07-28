def large_small_same():
    '''
    2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램을 작성하라.

    [입력]
    가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
    각 테스트 케이스의 첫 번째 줄에는 2개의 수가 주어진다.

    [출력]
    출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
    (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
    '''
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