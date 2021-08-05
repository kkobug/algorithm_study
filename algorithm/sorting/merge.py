def divide(num_list):
    if len(num_list) <= 1:
        return num_list
    
    mid = len(num_list) // 2
    left = divide(num_list[:mid])
    right = divide(num_list[mid:])
    return merge(left, right)

def merge(left, right):
    result = [] # 공간복잡도 2N
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0: # 둘다 값을 가질 때
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0: # 왼쪽만 값을 가질 때
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0: # 오른쪽만 값을 가질 때
            result.append(right[0])
            right = right[1:]
    return result

print(divide([4, 3, 2, 1, 0]))