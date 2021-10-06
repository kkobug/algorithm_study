"""
※ SW Expert 아카데미의 문제를 무단 복제하는 것을 금지합니다.

0부터 9까지인 숫자 카드 4세트를 섞은 후 6개의 카드를 골랐을 때,
연속인 숫자가 3개 이상이면 run, 같은 숫자가 3개 이상이면 triplet이라고 한다.
게임을 시작하면 플레이어1과 플레이어 2가 교대로 한 장 씩 카드를 가져가며,
6장을 채우기 전이라도 먼저 run이나 triplet이 되는 사람이 승자가 된다.
두 사람이 가져가게 되는 순서대로 12장의 카드에 대한 정보가 주어졌을 때 승자를 알아내는 프로그램을 작성하시오.
만약 무승부인 경우 0을 출력한다.
예를 들어 9 9 5 6 5 6 1 1 4 2 2 1인 경우, 플레이어 1은 9, 5, 5, 1, 4, 2카드를, 플레이어2는 9, 6, 6, 1, 2, 1을 가져가게 된다.
이때는 카드를 모두 가져갈 때 까지 run이나 triplet이 없으므로 무승부가 된다.

[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 각 줄에 0에서 9사이인 12개의 숫자가 주어진다.

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

입력
3
9 9 5 6 5 6 1 1 4 2 2 1
5 3 2 9 1 5 2 0 9 2 0 0
2 8 7 7 0 2 2 2 5 4 0 3
출력
#1 0
#2 1
#3 2
"""
def is_gin(X):  # 승부
    i = 0
    while i < 10:
        if X[i] >= 3:  # triplet
            return True
        elif i >= 2 and X[i-2] and X[i-1] and X[i]:  # run
            return True
        i += 1
    return False

for tc in range(1, 1+int(input())):
    cards = list(map(int, input().split()))
    A = cards[::2]  # 카드 분배
    A_cnt = [0] * 10
    B = cards[1::2]
    B_cnt = [0] * 10
    ans = 0
    for i in range(6):
        A_cnt[A[i]] += 1  # 카드 카운팅
        B_cnt[B[i]] += 1
        if i < 2:
            continue

        a = is_gin(A_cnt)
        if a:
            ans = 1
            break
        b = is_gin(B_cnt)
        if b:
            ans = 2
            break

    print(f'#{tc} {ans}')