def num_reverse():
    '''
    0까지 거꾸로 찍기
    '''
    x = int(input())
    result = []
    while x >= 0:
        result.append(str(x))
        x -= 1
    return ' '.join(result)

print(num_reverse())