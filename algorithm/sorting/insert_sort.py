"""
두 번째 인덱스부터 마지막까지 반복하며
i번째 인덱스의 앞의 인덱스들을 모두 비교하여 i번째 인덱스의 크기가 더 작아지는 위치에서 삽입
"""


arr = [4, 1, 2, 3, 0]
def insert_sort(num_list):
    for i in range(1, len(num_list)):
        data = num_list[i]
        j = i
        while j > 0 and num_list[j-1] > data:
            num_list[j] = num_list[j-1]
            j -= 1
        num_list[j] = data
    return num_list

print(insert_sort(arr))