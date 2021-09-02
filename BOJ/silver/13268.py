"""
문제
다현이는 사악하다. 겉과는 다르게 다현이는 주변사람들이 힘들어 하는걸 즐긴다.
동아리의 총무인 다현이는 돈으로 협박하여 회장인 지훈이를 괴롭히려 한다.
그녀는 물질적 공갈으로 성이 차지 않아 육체적 고통을, 셔틀런을 시킬 것이다.
심지어 보통 셔틀런이 아니다. 흔히 <수어사이드>라 불리는 고통스러운 셔틀런이다. 방식은 이렇다.

시작점부터 약 5m 의 간격을 두고 직선 상으로 총 4 개의 연습용 콘을 세워둔다.
따라서 마지막 콘은 시작점부터 20m 떨어져있다. 그러면 지훈이는 시작점부터 첫 번째 콘까지 달린 후 시작점으로 다시 돌아온다.
이제 두 번째 콘까지 달린 후 다시 시작점으로 뛰어온다. 세 번째 콘과 네 번째 콘에 대해서도 순서대로 똑같이 한다.

보통은 한 세트를 뛰고 나면 일정 시간 쉬는 것이 정상이지만, 다현이는 그런 여유를 지훈이에게 줄 생각이 없다.
따라서 네 번째 콘을 찍고 시작점으로 돌아오자 마자 지훈이는 다시 첫 번째 콘을 향해 달려야 한다.
불쌍한 지훈이는 쓰러질 때까지 무한히 반복해야 한다.

지훈이가 쓰러지기 전까지 달릴 수 있는 거리가 주어졌을 때 지훈이가 어느 구간에서 쓰러졌는지 찾아서 지훈이를 구하러 가자.

입력
첫째 줄에 지훈이가 쓰러지기 전까지 달릴 수 있는 거리(10000 이하의 자연수)가 주어진다.

출력
지훈이가 쓰러진 구간을 하나의 숫자로 출력한다.
시작점을 구간 0, 시작점부터 (시작점 미포함)
첫 번째 콘까지 (첫 번째 콘 포함) 구간을 1,
첫 번째 콘 (미포함) 부터 두 번째 콘까지 (포함) 구간을 2, 등으로 표기한다.

예제 입력 1
7
예제 출력 1
1
"""
N = int(input())
flag = True
while flag:
    for i in range(1, 5):  # 1 ~ 5구간 왕복 가능할 때 까지 갔다오기
        if i * 10 < N:
            N -= i * 10
        else:
            flag = False
            break

if N == i * 10 or not N:  # 남은 거리는 N, 가야하는 구간은 i개
    print(0)  # 남은 거리가 없거나, 남은 거리가 가야할 거리가 같으면 0

else:
    if i * 5 < N:  # 돌아오는 길에 쓰러지면
        ans = ((i*10+4)-N)//5
    else:  # 가는 길에 쓰러지면
        ans = (N+4)//5
    print(ans)
