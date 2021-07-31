def gauss_sum(x):
    '''
    가우스합 구하기
    sol1. 재귀함수
    '''
    if x <= 1:
        return 1
    else:
        return gauss_sum(x-1) + x
    
def gauss_sum_2(x):
    '''
    가우스합 구하기
    soil2. 반복문
    '''
    result = 0
    for i in range(1, 1+x):
        result += i
    return result


x = int(input())

print(gauss_sum(x))
print(gauss_sum_2(x))