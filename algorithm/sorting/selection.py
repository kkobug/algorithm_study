"""
첫 번째 인덱스부터 마지막 직전 인덱스까지 반복
i번째 인덱스와 i+1번째 인덱스 ~ 마지막 인덱스 까지 비교하여 크기가 작은 것을 i번째로 이동
"""


def selection(num_list):
    for i in range(len(num_list)-1):
        temp = i
        for j in range(i+1, len(num_list)):
            if num_list[temp] > num_list[j]:
                temp = j
        num_list[i], num_list[temp] = num_list[temp], num_list[i]

    return num_list


print(selection([4, 3, 2, 1, 0]))