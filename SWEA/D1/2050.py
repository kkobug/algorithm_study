def alpha_to_digit():
    '''
    알파벳을 숫자로 변환하여 출력하기
    ※ 알파벳이 아닌 입력 구분할 것
    sol1. 모두 대문자로 바꿔서 변환 (ㅇ)
    sol2. 대/소문자 조건문으로 거르기
    '''
    alphabet = list(input())
    result = []
    #알파벳 리스트를 만들면 아스키코드 없이 풀 수 있다.
    
    for a in alphabet:
        if a.isalpha():
            result.append(str(ord(a.upper())-64))
        else:
            return print('알파벳이 아닙니다.')

    return ' '.join(result)

print(alpha_to_digit())