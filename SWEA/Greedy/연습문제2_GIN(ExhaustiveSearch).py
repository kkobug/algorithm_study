# 6자리 숫자에 대해 완전검색을 적용하여 Baby-gin 검사
"""
예시 입력
124783
667767
054060
101123
"""

def check(a, b, c):
    if a == b and b == c:
        return True
    if a+1 == b and b+1 == c:
        return True
    return False


def baby_gin(v, idx=0):
    global gin
    if gin:
        return
    if idx == N:
        if check(ans[0], ans[1], ans[2]) and check(ans[3], ans[4], ans[5]):
            gin = True
        return

    for i in range(N):
        if v[i]:
            continue
        v[i] = True
        ans.append(arr[i])
        baby_gin(v, idx+1)
        v[i] = False
        ans.pop()




N = 6
arr = list(map(int, list(input())))
ans = []
gin = False
visit = [False]*6
baby_gin(visit)
print(gin)