def small_to_capital():
    '''
    소문자를 대문자로 바꾸기
    * 알파벳이 아닌 문자 포함 가능
    sol1. 모두 대문자로 바꿔서 변환
    sol2. 대/소문자 조건문으로 거르기 (ㅇ)
    '''
    title = list(input())
    result = []

    for t in title:
        if 97 <= ord(t) <= 122:
            result.append(chr(ord(t)-32))
        else:
            result.append(t)
    
    return ''.join(result)

print(small_to_capital())