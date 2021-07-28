def each_sum():
    '''
    하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램을 작성하라.

    [입력]
    입력으로 자연수 N이 주어진다.

    [출력]
    각 자릿수의 합을 출력한다.
    '''
    N = int(input())
    result = 0
    while N > 0:
        result += N % 10
        N = N // 10
    return result

print(each_sum())