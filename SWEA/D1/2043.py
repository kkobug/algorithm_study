def password():
    '''
    K가 1씩 증가할 때, P와 같아지려면 얼마나 증가하는가
    조건1. P와 K의 범위는 000 ~ 999
    조건2. 입력은 항상 3자리(자물쇠는 012 != 12)

    Hidden case: P < K
    ex
    999 0 > 1000
    0 999 > 2
    '''
    PK = list(input().split(' '))

    if len(PK[0]) == 3 and len(PK[1]) == 3:
        PK = list(map(int, PK))

        if PK[0] >= PK[1]:
            return PK[0] - PK[1] + 1
        return PK[0] + 1000 - PK[1] + 1
        
    return '입력이 잘못되었습니다.'

print(password())