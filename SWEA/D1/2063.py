def what_is_mid():
    '''
    중간값은 통계 집단의 수치를 크기 순으로 배열 했을 때 전체의 중앙에 위치하는 수치를 뜻한다.
    입력으로 N 개의 점수가 주어졌을 때, 중간값을 출력하라.

    [제약 사항]
    1. N은 항상 홀수로 주어진다.
    2. N은 9이상 199 이하의 정수이다. (9 ≤ N ≤ 199)

    [입력]
    입력은 첫 줄에 N 이 주어진다.
    둘째 줄에 N 개의 점수가 주어진다.

    [출력]
    N 개의 점수들 중, 중간값에 해당하는 점수를 정답으로 출력한다.
    '''
    N = int(input())
    num_list = list(map(int, input().split()))
    for i in range(len(num_list)):
        for j in range(len(num_list)-1):
            if num_list[j] >= num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    return num_list[N//2]

print(what_is_mid())