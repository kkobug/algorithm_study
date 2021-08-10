def min_max():
    """
    N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.

    [입력]
    첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )
    각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )
    다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )

    [출력]
    각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
    """
    T = int(input())
    for tc in range(1, T + 1):
        length = int(input())
        numbers = list(map(int, input().strip().split()))
        for i in range(length - 1, 0, -1):
            for j in range(i):
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        result = numbers[-1] - numbers[0]
        print("#{} {}".format(tc, result))


min_max()
