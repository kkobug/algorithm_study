"""
자료의 가운데 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하여 검색
검색 위치를 절반씩 줄여나가며 검색
정렬된 경우에만 사용 가능
"""

# find index of 3
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def binary_search(arr, key):
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            end = mid -1
        else:
            start = mid + 1
    return -1

print(binary_search(num_list, 3))