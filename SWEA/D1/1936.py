def r_s_p(x, y):
    '''
    3은 2를, 2는 1을, 1은 3을 이긴다
    '''
    if x in [1, 2, 3] and y in [1, 2, 3]:
        if x == y:
            return 'DRAW'
        if x - y == 1 or x - y == -2:
            return 'A'
        else:
            return 'B'
    return '입력이 잘못되었습니다.'

num = list(map(int, input().split(' ')))
print(r_s_p(num[0], num[1]))