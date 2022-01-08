"""
분할이 가능할 때 까지 분할한 후, 병합할 때 크기를 정렬하여 병합
Divide & Conquer 방식을 이용하는데, Divide 부분과 Conquer(merge) 부분을 나누어도 되고, 합쳐서 작성해도 된다.
리스트의 분할과 병합은 메모리가 많이 소모되므로, 인덱스만을 이용해 병합정렬을 하기도 한다.
각 방법을 모두 구현해보도록 한다
1. divide, merge 나누어 구현하기
2. divide, merge 통합하여 하나로 구현하되, 리스트가 아닌 인덱스를 활용하여 구현하기
"""


arr = [4, 4, 1, 1, 2, 2, 3, 3, 0, 0]
N = len(arr)


# 1. Divide & Conquer 나누어 구현하기
def divide(num_list):  # Divide 부분
    if len(num_list) <= 1:
        return num_list
    
    mid = len(num_list) // 2
    left = divide(num_list[:mid])
    right = divide(num_list[mid:])
    return merge(left, right)


def merge(left, right):
    result = []  # 공간복잡도 2N
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:  # 둘다 값을 가질 때
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]  # 여기서 시간을 많이 사용하게 될 것
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:  # 왼쪽만 값을 가질 때
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:  # 오른쪽만 값을 가질 때
            result.append(right[0])
            right = right[1:]
    return result


print(divide(arr))


# 2. 통합하여 구현하고, 인덱스를 활용하기: slicing에 걸리는 시간이 줄어듦
def merge_sort(num_list):
    if len(num_list) <= 1:
        return num_list

    mid = len(num_list) // 2
    L = merge_sort(num_list[:mid])
    R = merge_sort(num_list[mid:])

    ret = []
    len_L, len_R = len(L), len(R)
    idx_L = idx_R = 0
    while idx_L < len_L or idx_R < len_R:
        if idx_L < len_L and idx_R < len_R:
            if L[idx_L] < R[idx_R]:
                ret.append(L[idx_L])
                idx_L += 1
            else:
                ret.append(R[idx_R])
                idx_R += 1
        elif idx_L < len_L:
            ret.append(L[idx_L])
            idx_L += 1
        elif idx_R < len_R:
            ret.append(R[idx_R])
            idx_R += 1
    return ret


print(merge_sort(arr))
