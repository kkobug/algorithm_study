"""
https://www.acmicpc.net/problem/1654
"""
K, N = map(int, input().split())
lans = []
st = 1
ed = 1000000
for _ in range(K):
    lan = int(input())
    if ed < lan:
        ed = lan
    lans.append(lan)
ed += 1

while st < ed:
    mid = (st + ed) // 2
    lan = 0
    for k in range(K):
        lan += lans[k] // mid
    
    # 얻고자 하는 개수가 나오면 더 길게 자르고
    if N <= lan:
        st = mid+1
    # 아니면 더 짧게 자르기
    else:
        ed = mid

print(ed-1)