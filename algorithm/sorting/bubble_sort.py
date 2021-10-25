"""
<오름차순>
마지막 인덱스 부터 2번째 인덱스 까지 반복
j번째 인덱스와 j+1번째 인덱스를 비교하여 크기가 큰 것을 뒤로 이동
i 기준 1회 반복 때 마다 가장 큰 값이 맨 뒤로 밀려나므로 j 반복문의 반복길이가 1씩 감소
"""


arr = [4, 1, 2, 3, 0]
def bubble_sort(num_list):
    for i in range(len(num_list)-1, 0, -1):
        for j in range(0, i):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]

    return num_list


print(bubble_sort(arr))