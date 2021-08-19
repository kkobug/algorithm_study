# exp = input()
# ans, cnt = 0, 0
# text = ''
# for i in range(len(exp)):
#     if exp[i] in '0123456789':
#         text += exp[i]
#     elif exp[i] == '+' and cnt == 0:
#         ans += int(text)
#         text = ''
#     elif exp[i] == '-' and cnt == 0:
#         ans += int(text)
#         text = ''
#         cnt += 1
#     elif cnt:
#         ans -= int(text)
#         text = ''

# print(ans-int(text))

num = input().split('-')

result = 0
for i in num[0].split('+'):
    result += int(i)

for j in num[1:]:
    for k in j.split('+'):
        result -= int(k)


print(result)