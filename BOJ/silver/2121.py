# d = int(input())
# x, y = map(int, input().split())
# dots = []
# for _ in range(d):
#     dot = list(map(int, input().split()))
#     if dot not in dots:
#         dots.append(dot)
# cnt = 0
# for i in dots:
#     if [i[0]+x, i[1]] in dots and [i[0]+x, i[1]+y] in dots and [i[0], i[1]+y] in dots:
#         cnt += 1
#
# print(cnt)





"""
절취선
"""
d = int(input())
x, y = map(int, input().split())
dots = {}
ans = 0
for _ in range(d):
    a, b = map(int, input().split())
    if dots.get(a):
        dots[a].add(b)
    else:
        dots[a] = {b}

for k in dots:
    if dots.get(k+x):
        for v in dots[k]:
            if v in dots[k+x]:
                if v+y in dots[k]:
                    if v+y in dots[k+x]:
                        ans += 1

print(ans)
"""
절취선
"""






# d = int(input())
# x, y = map(int, input().split())
# ans = 0
# dot = [tuple(map(int, input().split())) for _ in range(d)]
# dots = set(dot)
#
# res = 0
# for i in dots:
#     if (i[0] + x, i[1]) in dots and (i[0] + x, i[1] + y) in dots and (i[0], i[1] + y) in dots:
#         res += 1
#
# print(res)