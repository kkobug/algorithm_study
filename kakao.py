# 1
# def solution(id_list, report, k):
#     answer = []
#     user = {}
#     ban = []
#     for i in range(len(id_list)):
#         user[id_list[i]] = [0]
#
#     for i in set(report):
#         i = i.split()
#         repo, reported = i[0], i[1]
#         user[repo].append(reported)
#         user[reported][0] += 1
#
#     for i in user:
#         if user[i][0] >= k:
#             ban.append(i)
#
#     for i in user.values():
#         temp = 0
#         for j in ban:
#             if j in i:
#                 temp += 1
#         answer.append(temp)
#     print(answer)
#     return answer
#
#
# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# k = 2
# solution(id_list, report, k)

# 2
# def prime_n(N):
#     if N < 2:
#         return False
#     for p in range(2, int(N**0.5)+1):
#         if N % p == 0:
#             return False
#     return True
#
# def solution(n, k):
#     answer = 0
#     num = 0
#     cnt = 1
#     if k == 10:
#         num = n
#     else:
#         while n > 0:
#             num += (n % k) * cnt
#             cnt *= 10
#             n //= k
#
#     temp = 0
#     cnt = 1
#     while num:
#         if num % 10 == 0:
#             if temp:
#                 if prime_n(temp):
#                     answer += 1
#                 temp = 0
#                 cnt = 1
#         else:
#             temp += cnt*(num % 10)
#             cnt *= 10
#         num //= 10
#
#     if temp:
#         if prime_n(temp):
#             answer += 1
#
#     return answer
#
# n = 437674
# k = 3
# print(solution(n, k))
#
# n = 110011
# k = 10
# print(solution(n, k))

# 3
# def solution(fees, records):
#     answer = []
#     cars = {}
#     for i in records:
#         t, num, drive = i.split()
#
#         if not cars.get(num):
#             cars[num] = [0, 0]
#
#         if drive == "IN":
#             cars[num].append(t)
#         else:
#             in_time = cars[num].pop()
#             dur = (int(t[:2]) - int(in_time[:2])) * 60 + (int(t[3:]) - int(in_time[3:]))
#             cars[num][0] += dur
#
#
#     for v in cars.values():
#         if len(v) > 2:
#             in_time = v.pop()
#             dur = (23 - int(in_time[:2])) * 60 + (59 - int(in_time[3:]))
#             v[0] += dur
#
#         v[1] += fees[1]
#         if v[0] > fees[0]:
#             v[0] -= fees[0]
#             v[1] += fees[3] * (v[0]//fees[2])
#             if v[0] % fees[2]:
#                 v[1] += fees[3]
#
#     temp = sorted(cars.items())
#
#     for ans in temp:
#         answer.append(ans[1][1])
#
#     return answer
#
#
# fees = [180, 5000, 10, 600]
# records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
# print(solution(fees, records))

# 4
def solution(n, info):
    length = len(info)
    answer = [0] * length
    score = [0] * length
    for i in range(length):
        if info[i]:
            score[i] = ((length - i)*2 / (info[i] + 1), info[i] + 1, length - i)
        else:
            score[i] = ((length - i) / (info[i] + 1), info[i] + 1, length - i)
    score.sort(reverse=True)
    while n > 0:
        for i in range(length):
            if not answer[i]:
                if n >= score[i][1]:
                    n -= score[i][1]
                    answer[length - score[i][2]] += score[i][1]
        if n >= score[-1][1]:
            n -= score[-1][1]
            answer[length - score[-1][2]] += score[-1][1]
        answer[-1] = n

    # print(score)
    tempA = 0
    tempR = 0
    for i in range(9):
        if info[i]:
            if not answer[i]:
                tempA += length-i
        if answer[i]:
            tempR += length-i
    if tempR <= tempA:
        answer = [-1]
    return answer

n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]
print(solution(n, info))
n = 1
info = [1,0,0,0,0,0,0,0,0,0,0]
print(solution(n, info))
n = 9
info = [0,0,1,2,0,1,1,1,1,1,1]
print(solution(n, info))
n = 10
info = [0,0,0,0,0,0,0,0,3,4,3]
print(solution(n, info))

"""
n	info	result
5	[2,1,1,1,0,0,0,0,0,0,0]	[0,2,2,0,1,0,0,0,0,0,0]
1	[1,0,0,0,0,0,0,0,0,0,0]	[-1]
9	[0,0,1,2,0,1,1,1,1,1,1]	[1,1,2,0,1,2,2,0,0,0,0]
10	[0,0,0,0,0,0,0,0,3,4,3]	[1,1,1,1,1,1,1,1,0,0,2]
"""

# 6
# def solution(board, skill):
#     answer = 0
#
#     for s in skill:
#         if s[0] == 1:
#             for i in range(s[1], s[3]+1):
#                 for j in range(s[2], s[4]+1):
#                     board[i][j] -= s[5]
#         else:
#             for i in range(s[1], s[3]+1):
#                 for j in range(s[2], s[4]+1):
#                     board[i][j] += s[5]
#
#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             if board[i][j] > 0:
#                 answer += 1
#
#     return answer
#
# board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
# skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
# print(solution(board, skill))
