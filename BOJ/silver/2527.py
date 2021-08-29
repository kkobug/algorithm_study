"""
문제
x2차원 격자공간에 두 개의 꼭짓점 좌표로 표현되는 직사각형이 있다.
직사각형은 왼쪽 아래 꼭짓점 좌표 (x, y)와 오른쪽 위 꼭짓점 좌표 (p, q)로  주어진다.
이 문제에서 모든 직사각형은 두 꼭짓점의 좌표를 나타내는 4개의 정수 x y p q 로 표현된다.
단 항상 x<p, y<q 이다.

직사각형의 겹치는 부분이 직사각형인지, 선분인지, 점인지, 아니면 전혀 없는 지를 판별해서 해당되는 코드 문자를 출력한다.

공통부분의 특성: 코드 문자
직사각형: a
선분: b
점: c
공통부분이 없음: d
입력
4개의 줄로 이루어져 있다.
각 줄에는  8개의 정수가 하나의 공백을 두고 나타나는데,
첫 4개의 정수는 첫 번째 직사각형을,
나머지 4개의 정수는 두 번째 직사각형을 각각 나타낸다.
단 입력 직사각형의 좌표 값은 1이상 50,000 이하의 정수로 제한된다.

출력
4개의 각 줄에 주어진 두 직사각형의 공통부분에 해당하는 코드 문자를 출력파일의 첫 4개의 줄에 각각 차례대로 출력해야 한다.

예제 입력 1
3 10 50 60 100 100 200 300
45 50 600 600 400 450 500 543
11 120 120 230 50 40 60 440
35 56 67 90 67 80 500 600

예제 출력 1
d
a
a
b
"""

def isoverlap():
    if (p1, q1) == (x2, y2):
        return 'c'
    elif (x1, y1) == (p2, q2):
        return 'c'
    elif (x1, q1) == (p2, y2):
        return 'c'
    elif (p1, y1) == (x2, q2):
        return 'c'

    if q1 == y2 and p1 > x2 and x1 < p2:
        return 'b'
    elif y1 == q2 and p1 > x2 and x1 < p2:
        return 'b'
    elif p1 == x2 and q1 > y2 and y1 < q2:
        return 'b'
    elif x1 == p2 and q1 > y2 and y1 < q2:
        return 'b'

    if p1 < x2:
        return 'd'
    elif p2 < x1:
        return 'd'
    elif q1 < y2:
        return 'd'
    elif q2 < y1:
        return 'd'

    return 'a'


for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    print(isoverlap())