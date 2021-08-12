def bisection(N, A, B):
    """
    코딩반 학생들에게 이진 탐색을 설명하던 선생님은 이진탐색을 연습할 수 있는 게임을 시켜 보기로 했다.
    짝을 이룬 A, B 두 사람에게 교과서에서 각자 찾을 쪽 번호를 알려주면, 이진 탐색만으로 지정된 페이지를 먼저 펼치는 사람이 이기는 게임이다.
    예를 들어 책이 총 400쪽이면, 검색 구간의 왼쪽 l=1, 오른쪽 r=400이 되고, 중간 페이지 c= int((l+r)/2)로 계산한다.
    찾는 쪽 번호가 c와 같아지면 탐색을 끝낸다.
    책의 전체 쪽수와 두 사람이 찾을 쪽 번호가 주어졌을 때, 이진 탐색 게임에서 이긴 사람이 누구인지 알아내 출력하시오. 비긴 경우는 0을 출력한다.

    [입력]
    첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
    테스트 케이스 별로 책의 전체 쪽 수 P, A, B가 찾을 쪽 번호 Pa, Pb가 차례로 주어진다. 1<= P, Pa, Pb <=1000

    [출력]
    각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, A, B, 0 중 하나를 출력한다.
    """
    if N == A: return 'A'
    elif N == B: return 'B'

    l_a, r_a = 1, N
    l_b, r_b = 1, N
    c_a, c_b = 0, 0
    while True:
        mid_a = (l_a + r_a)//2
        if A > mid_a:
            l_a = mid_a
        elif A < mid_a:
            r_a = mid_a
        else:
            c_a = mid_a

        mid_b = (l_b + r_b)//2
        if B > mid_b:
            l_b = mid_b
        elif B < mid_b:
            r_b = mid_b
        else:
            c_b = mid_b

        if c_a == A and c_b == B:
            return 0
        elif c_a == A:
            return 'A'
        elif c_b == B:
            return 'B'


for tc in range(1, 1 + int(input())):
    N, A, B = map(int, input().split())
    print("#{} {}".format(tc, bisection(N, A, B)))

