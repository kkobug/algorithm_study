"""
연습문제 1
새로운 bit 단위로 묶어 10진수로 바꾸기

입력
00000010001101
출력
1
13

입력
0000000111100000011000000111100110000110000111100111100111111001100111
출력
??
"""
def bit_print(n):
    ret = 0
    k = 1
    for j in range(len(n)-1, -1, -1):  # 자릿수 비교하며 10진수로 바꾸기
        if n[j] == "1":
            ret += k
        k *= 2
    print(ret)


x = input()
cut = 7
for i in range(0, len(x), cut):
    bit_print(x[i:i+cut])
