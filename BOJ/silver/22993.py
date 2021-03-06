"""
문제
넥슨의 게임 개발자 준원이는 서든어택 3의 출시를 앞두고 게임 테스트를 하고 있다.
맵에는 준원이를 포함해 $N$명의 플레이어가 있다. 준원이의 공격력은 A1이고,나머지 사람들의 공격력은 A2, ..., AN이다.
전투가 시작되면 누구나 누구든 공격할 수 있게 된다!
죽은 사람은 공격하거나 공격받지 못하고, 두 사람이 동시에 공격하는 일은 일어나지 않는다.
공격력이 X인 플레이어 A가 공격력이 Y인 플레이어 B를 공격하면,
X > Y 이면, B가 죽고 A의 공격력은 X+Y가 된다.
X < Y 이면, A가 죽고 B의 공격력은 X+Y가 된다.
X = Y 이면, 아무 일도 일어나지 않는다.
드디어 전투가 시작되었다! 준원이는 최후의 생존자가 될 수 있을까?

입력
첫째 줄에는 준원이를 포함한 플레이어의 수 N이 주어진다.

둘째 줄에는 각 플레이어의 공격력 A1, ..., AN이 차례대로 공백을 사이에 두고 주어진다.

출력
좋은 전투 순서가 존재해서 준원이만 생존하고 나머지 플레이어가 모두 죽게 만들 수 있다면 Yes를,
반대로 전투가 어떤 순서로 이루어져도 준원이가 절대 최후의 생존자가 될 수 없다면 No를 출력한다.

제한
1 <= N <= 100000
1 <= Ai <= 1000000000 (1 <= i <= N)

예제 입력 1
5
2 1 2 3 4
예제 출력 1
Yes
"""
from sys import stdin as st

N = int(st.readline())

players = list(map(int, st.readline().split()))
joon = players.pop(0)
players.sort()
ans = "Yes"

for i in players:
    if joon > i:
        joon += i
    else:
        ans = "No"
        break

print(ans)