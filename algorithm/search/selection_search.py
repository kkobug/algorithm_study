"""
저장된 자료의 k번째 원소를 찾는 방법
정렬 알고리즘을 이용하여 자료를 정렬한 후, 원하는 순서에 있는 원소를 가져온다.
선택정렬을 사용할 시, 정렬을 끝까지 시행하지 않아도 탐색 가능
"""

# find data of nth (ex. 2rd(=3)
num_list = [5, 2, 6, 3, 7, 11, 4]
n = 2


def selection_search(arr, n):
    for i in range(n):
        temp = i
        for j in range(i+1, len(num_list)):
            if num_list[temp] > num_list[j]:
                temp = j
        num_list[i], num_list[temp] = num_list[temp], num_list[i]
    return arr[n-1]


print(selection_search(num_list, n))