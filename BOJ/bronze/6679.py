"""
문제
싱기한 네자리 숫자란, [1000,9999]인 10진수 숫자중에서,  다음의 조건을 만족하는 숫자를 말한다.

숫자를 10진수, 12진수, 16진수로 나타낸 다음, 각각의 숫자에 대해, 각 숫자의 자리수를 더했을 때, 세 값이 모두 같아야 한다.
여러분은 싱기한 네자리 숫자를 모두 출력해야 한다.

입력
입력은 주어지지 않는다.

출력
싱기한 네자리 숫자를 오름차순으로 한줄에 하나씩 출력한다.
"""
def sum_digit(num, n):
    ans = 0
    while num:
        ans += num%n
        num //= n
    return ans

for i in range(1000, 10000):
    temp = sum_digit(i, 10)
    if temp == sum_digit(i, 12) and temp == sum_digit(i, 16):
        print(i)