"""
연습문제 2
16진수를 2진수로 바꾼 후, 새로운 bit 단위로 묶어 10진수로 바꾸기

입력
0F97A3
출력
7
101
116
3

입력
01D06079861D79F99F
출력
??
"""
def bit_print(n):  # 연습문제 1과 같은 과정
    ans = 0
    k = 1
    for j in range(len(n)-1, -1, -1):
        if n[j] == "1":
            ans += k
        k *= 2
    print(ans)

hex_change = {
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
}
x = input()
hex_num = ''
cut = 7
for i in x:
    ret = ''
    if 'A' <= i <= 'F':
        num = hex_change[i]
    else:
        num = int(i)

    temp = 8
    for j in range(4):
        if (temp >> j) & num:
            ret += '1'
        else:
            ret += '0'  # 무조건 4자리를 채워야하므로

    hex_num += ret

for i in range(0, len(hex_num), cut):
    bit_print(hex_num[i:i+cut])
