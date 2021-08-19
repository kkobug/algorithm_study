# 소인수 개수 구하기
# def small_num(num):
#     div = 2
#     cnt = 0
#     lim = num // 2
#     while div <= lim:
#         if num % div == 0:
#             cnt += 1
#             num /= div
#         else:
#             div += 1
#     return cnt

"""
절취선
"""

A, B = map(int, input().split())
ans = 0

# 소수 판독기 memo
prime = [0, 0] + [1]*(B-1)
for pr in range(2, int(B**0.5)+1):
    if prime[pr]:
        for p in range(2*pr, B+1, pr):
            prime[p] = 0

small = prime[:]  # 소수만 1 필요없엉
for i in range(2, B+1):
    if not small[i]:  # 합성수만 선택
        for j in range(2, B+1):
            if not i % j:
                small[i] = small[i//j] + 1
                break
                # ex. 12 [1 2 3 4 6 12]
                #        [1 2 3 4 6 12]

for a in range(A, B+1):
    if prime[small[a]]: ans += 1 # 1보다 큰거만

print(ans)

"""
절취선
"""

# A, B = map(int, input().split())
# prime = [0, 0] + [1]*(B-1)
# ans = 0
# for pr in range(2, int(B**0.5)+1):
#     if prime[pr]:
#         for p in range(2*pr, B+1, pr):
#             prime[p] = 0
#
# small = prime[:]
# for i in range(2, B+1):
#     if prime[i]:
#         for j in range(2, B+1):
#             if i*j > B: break  # 이거 있으면 O(N)?
#             small[i*j] = small[j] + 1
#
# for a in range(A, B+1):
#     if prime[small[a]]: ans += 1
#
# print(ans)

"""
절취선
"""