"""
https://programmers.co.kr/learn/courses/30/lessons/77886
"""
def solution(s):
    answer = []
    for number in s:
        removed_list = []
        moved_list = []
        for i in number:
            removed_list.append(i)
            if len(removed_list) < 3:
                continue

            if removed_list[-1] == "0" and removed_list[-2] == "1" and removed_list[-3] == "1":
                del removed_list[-3:]
                moved_list.append("110")

        mid_point = 0
        for i in range(len(removed_list)-1, -1, -1):
            if removed_list[i] == "0":
                mid_point = i+1
                break
        answer.append("".join(
            removed_list[:mid_point] + moved_list + removed_list[mid_point:]
        ))
    return answer


print(solution(["1110","100111100","0111111010", "1111", "0000", "111", "000", "110", "11", "00", "1", "0", "00110", "11011", "11000"]))
