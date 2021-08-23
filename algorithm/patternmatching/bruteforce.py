"""
문자열을 처음부터 끝까지 순회하며 원하는 패턴의 문자열이 있는지 일일이 비교하는 알고리즘
두 문자열의 모든 위치에서 패턴을 비교하므로 시간복잡도는 O(MN)
"""

M = "BRUTEFORCEALGORITHM"
N = "RCEAL"


def bruteforce(origin, pattern):
    i, j = 0, 0
    while i < len(origin):
        if origin[i] != pattern[j]:
            i -= j
            j = -1
        i += 1
        j += 1
        if j == len(pattern):
            return i - len(pattern)
    return -1


print(bruteforce(M, N))
