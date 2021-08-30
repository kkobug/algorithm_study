"""
시리얼번호를 비교하는 프로그램을 작성
1. 시리얼번호는 숫자와 알파벳 대문자로 구성
2. 시리얼번호의 길이가 짧은 것이 앞
3. 길이가 같다면 숫자의 자리수 합이 작은 것이 앞
4. 길이도 같고, 자리수 합도 같다면 사전순

예제 입력 1
5
ABCD
145C
A
A910
Z321
예제 출력 1
A
ABCD
Z321
145C
A910
"""
N = int(input())
serial = [input() for _ in range(N)]

serial.sort()

for i in range(N-1, -1, -1):
    for j in range(i):
        if len(serial[j]) > len(serial[j+1]):
            serial[j], serial[j + 1] = serial[j+1], serial[j]
            continue

        elif len(serial[j]) == len(serial[j+1]):
            temp_x = temp_y = 0
            for x in serial[j]:
                if ord('0') <= ord(x) <= ord('9'):
                    temp_x += int(x)

            for y in serial[j+1]:
                if ord('0') <= ord(y) <= ord('9'):
                    temp_y += int(y)

            if temp_x > temp_y:
                serial[j], serial[j + 1] = serial[j + 1], serial[j]

for p in serial:
    print(p)


"""
def intsum(element):
    ans = 0
    for i in element:
        if i.isdigit():
            ans += int(i)
    return ans

num = int(input())
lst = []
for i in range(num):
    element = input()
    lst.append(element)
    
lst.sort(key = lambda x: (len(x), intsum(x), x))

for i in lst:
    print(i)
"""