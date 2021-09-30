"""
SWEA : [S/W 문제해결 응용] 1일차 - 암호코드 스캔
"""
PW = {
    '0001101': 0, '0011001': 1,
    '0010011': 2, '0111101': 3,
    '0100011': 4, '0110001': 5,
    '0101111': 6, '0111011': 7,
    '0110111': 8, '0001011': 9,
}
def is_10(X):
    ret = 0
    for i in range(8):
        if i % 2:
            ret += X[i]
        else:
            ret += 3*X[i]
    if ret % 10:
        return False
    else:
        return True


for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())
    codes = list(set([bin(int(input(), 16))[2:].rstrip('0') for _ in range(N)]))
    ans = []  # 정답 코드모음
    for code in codes:
        while code:
            k = 1
            while True:
                l = len(code)  # 코드 개수 확인
                if l < 56*k:  # 부족한 자리 채우기
                    code = '0'*(56*k-l) + code
                idx = len(code) - k*56  # 검사 시작위치 셋팅
                eight_code = []  # 이번 정답은!
                for i in range(idx, len(code), k*7):  # 검사 시작
                    temp_c = code[i:i+k*7]
                    st = 0
                    temp = ''  # 코드 장바구니
                    for j in range(1, len(temp_c)):
                        if temp_c[j-1] != temp_c[j]:  # 0(1)에서 1(0)로 넘어가는 위치에서 체크
                            temp += (j-st)//k * temp_c[j-1]  # 자리수로 나눠서 장바구니 담기
                            st = j
                    temp += (k*7-st)//k * '1'  # 빈 장바구니 1로 채우기
                    info = PW.get(temp)  # 코드 검사
                    if info == None:  # 꽝!
                        break
                    eight_code.append(info)  # 꽝 아니면 이번 정답에 저장
                if info == None:  # 꽝이면 자리수 더해서 다시검사
                    k += 1
                    continue
                if eight_code not in ans and is_10(eight_code):  # 검증, 중복확인
                    ans.append(eight_code)
                code = code[:len(code)-56*k].rstrip('0')  # 검사 완료한 코드 버리기
                break  # k가 얼마일지 모르므로 무한검사
    ans = sum(map(sum, ans))
    print(f'#{tc} {ans}')
