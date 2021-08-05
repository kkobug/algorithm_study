def divisor(x):
    '''
    정수 입력받아 약수 반환
    '''
    result = []
    for i in range(1, x+1):
        if x % i == 0:
            result.append(str(i))
    
    return ' '.join(result)

x = int(input())
print(divisor(x))