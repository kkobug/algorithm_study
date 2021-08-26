"""
배열에 각 항목이 몇 개씩 있는지 카운팅한 후 정렬
int형 자료형(값이 index에 대응 가능해야함)에 대해서만 적용 가능
배열 내의 가장 큰 정수가 얼마인지 알고 있어야 함
배열 내 값들의 편차가 클 경우 비효율적
"""

nums = [0, 2, 2, 4, 4, 8]


# def counting(num_list):
#     max_value = num_list[0]
#     for i in num_list:
#         if i > max_value:
#             max_value = i
#     result = [0] * len(num_list)
#     counting_list = [0] * (max_value + 1)
#
#     for j in num_list:
#         counting_list[j] += 1
#
#     # 개수 채우기
#     for k in range(1, len(counting_list)):
#         counting_list[k] = counting_list[k] + counting_list[k - 1]
#
#     for r in range(len(num_list) - 1, -1, -1):
#         result[counting_list[num_list[r]] - 1] = num_list[r]
#         counting_list[num_list[r]] -= 1
#
#     return result
#
#
# print(counting(nums))


def counting(num_list):
    max_val = max(num_list)
    result = [0] * len(num_list)
    cnt_list = [0] * (max_val + 1)
    for i in num_list:
        cnt_list[i] += 1

    for j in range(max_val):
        cnt_list[j+1] = cnt_list[j] + cnt_list[j+1]

    for k in num_list[::-1]:
        result[cnt_list[k] - 1] = k
        cnt_list[k] -= 1

    return result

print(counting(nums))