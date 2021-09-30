"""
SWEA : [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드
"""
PW = {
    '0001101': 0, '0011001': 1,
    '0010011': 2, '0111101': 3,
    '0100011': 4, '0110001': 5,
    '0101111': 6, '0111011': 7,
    '0110111': 8, '0001011': 9,
}

for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())
    scan = [input() for _ in range(N)]
    code = []
    for i in range(N):
        temp = scan[i].rstrip('0')
        if not temp: continue
        st = len(temp) - 56
        for _ in range(8):
            info = temp[st:st+7]
            st += 7
            code.append(PW[info])
        check = 0
        for j in range(8):
            if j % 2:
                check += code[j]
            else:
                check += 3 * code[j]
        if check % 10:
            print(f'#{tc} {0}')
        else:
            print(f'#{tc} {sum(code)}')
        break