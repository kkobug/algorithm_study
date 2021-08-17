# def back():
#     for tc in range(1, 1+int(input())):
#         N = int(input())
#         stu = [list(map(int, input().split())) for _ in range(N)]
#         fin = [[0, 0] * N]
#         while stu:
#             for i in range(N):
#                 if 0 <= i < N-1 and stu[i][1] <= stu[i+1][0]:
#                     stu[i] = [0, 0]
#


print(bool([]))