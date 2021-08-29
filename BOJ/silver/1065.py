"""
문제
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

출력
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

예제 입력 1
110
예제 출력 1
99
"""
def one_num(n):
    cnt = 0

    if n <= 99:
        return n
    elif 99 < n < 1000:
        for i in range(100, n + 1):
            while i > 99:
                temp = i % 10
                i //= 10

                if temp - i % 10 == i % 10 - (i % 100) // 10:
                    cnt += 1
        return cnt + 99
    else:
        return one_num(999)


print(one_num(int(input())))