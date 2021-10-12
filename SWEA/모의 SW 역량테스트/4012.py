"""
경우의 수(조합)을 통해 N/2개를 선택한 후 2개의 시너지를 더하기
i,j와 j,i가 시너지 관계로 i와 j를 선택하면 i,j와 j,i가 능력치에 모두 더해질 때
N/2개로 나뉜 두 조합의 차이가 가장 작을 때 그 값을 출력

1
4
0 5 3 8
4 0 4 1
2 5 0 3
7 2 3 0

#1 2
유사문제 : 스타트와 링크
"""

def cook(A=[], idx=0):
    global ans

    if len(A) == N//2:
        B = list(set(range(N)) - set(A))
        temp_a = temp_b = 0
        for r in range(N//2-1):
            for c in range(r+1, N//2):
                temp_a += food[A[r]][A[c]] + food[A[c]][A[r]]
                temp_b += food[B[r]][B[c]] + food[B[c]][B[r]]
        ans = min(abs(temp_a-temp_b), ans)
        return

    for i in range(idx, N):
        A.append(i)
        cook(A, i+1)
        A.pop()
for tc in range(int(input())):
    N = int(input())
    food = [list(map(int, input().split())) for _ in range(N)]
    ans = 20000
    cook()
    print(f'#{tc+1} {ans}')

















# 스타트와 링크.
# def select(_cnt, _idx=0):
#     global min_val
#     if _cnt == N//2:
#         temp_val = 0
#         for i in range(N):
#             if check[i]:
#                 temp_val += v_sum[i]
#             else:
#                 temp_val -= h_sum[i]
#         if min_val > abs(temp_val):
#             min_val = abs(temp_val)
#         return
#
#     for i in range(_idx, N):
#         check[i] = True
#         select(_cnt+1, i+1)
#         check[i] = False
#
# for tc in range(int(input())):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     v_sum = [0]*N
#     h_sum = [0]*N
#     check = [False]*N   # A팀은 True, B팀은 False로 지정
#
#     for r in range(N):
#         for c in range(N):
#             v_sum[c] += arr[r][c]
#             h_sum[r] += arr[r][c]
#
#     min_val = 9876543210    # 최솟값을 구해야하므로 충분히 큰 값으로 지정
#
#     select(0)               # 재귀함수 실행
#
#     print(f'#{tc+1} {min_val}')
