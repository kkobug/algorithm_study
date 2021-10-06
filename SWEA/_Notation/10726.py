"""
정수 N, M 이 주어질 때, M의 이진수 표현의 마지막 N 비트가 모두 1로 켜져 있는지 아닌지를 판별하여 출력하라.

[입력]
첫 번째 줄에 테스트 케이스의 수 TC가 주어진다.
이후 TC개의 테스트 케이스가 새 줄로 구분되어 주어진다.
각 테스트 케이스는 다음과 같이 구성되었다.
첫 번째 줄에 정수 N, M이 주어진다. (1 ≤ N ≤ 30 , 0 ≤ M ≤ 108)
[출력]
각 테스트 케이스마다 한 줄씩
마지막 N개의 비트가 모두 켜져 있다면 ON
아니면 OFF 를 출력하라.

입력
5
4 0
4 30
4 47
5 31
5 62

출력
#1 OFF
#2 OFF
#3 ON
#4 ON
#5 OFF
"""
# for tc in range(1, 1+int(input())):
#     N, M = map(int, input().split())
#     ans = 'ON'
#     for i in range(N):
#         if not M%2:
#             ans = 'OFF'
#             break
#         M //= 2
#     print(f'#{tc} {ans}')


for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())
    M = bin(M)
    ans = 'OFF'
    if M[len(M)-N:] == '1'*N:
        ans = 'ON'
    print(f'#{tc} {ans}')