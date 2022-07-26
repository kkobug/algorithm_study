"""
https://school.programmers.co.kr/learn/courses/30/lessons/17682
"""
def solution(dartResult):
    ans_list = [0, 0, 0]
    idx = 0
    k = -1
    while idx < len(dartResult):
        if "0" <= dartResult[idx] <= "9":
            k += 1
            if dartResult[idx+1] == "0":
                idx += 1
                ans_list[k] += 10
            else:
                ans_list[k] += int(dartResult[idx])
        elif dartResult[idx] == "D":
            ans_list[k] **= 2
        elif dartResult[idx] == "T":
            ans_list[k] **= 3
        elif dartResult[idx] == "#":
            ans_list[k] *= -1
        elif dartResult[idx] == "*":
            ans_list[k] *= 2
            if 0 < k:
                ans_list[k-1] *= 2
        idx += 1
    answer = sum(ans_list)
    return answer


print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))

