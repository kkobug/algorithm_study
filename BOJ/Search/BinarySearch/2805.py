"""
https://www.acmicpc.net/problem/2805
"""
N, M = map(int, input().split())
trees = list(map(int, input().split()))
st = 0
ed = max(trees)

# 벌목 후 나무 길이가 얻고싶은 길이 이상인지 확인하기 위함
def is_OK(H):
    global N, M
    tree = 0
    for t in range(N):
        if H < trees[t]:
            tree += trees[t] - H
    if M <= tree:
        return True
    return False


while st < ed:
    mid = (st + ed) // 2
    
    # 얻고자 하는 길이가 된다면 더 위를 자르고
    if is_OK(mid):
        st = mid+1
    # 얻고자 하는 길이가 안되면 더 아래를 잘라야함
    else:
        ed = mid

print(st-1)