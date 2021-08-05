def double(x):
    '''
    1부터 2^x까지 출력
    '''
    result = []
    for i in range(x+1):
        result.append(str(2**i))
    return ' '.join(result)

x = int(input())
print(double(x))