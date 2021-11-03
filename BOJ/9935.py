ans = []
words = input()
key = input()
length = len(key)
last = key[-1]
for word in words:
    ans.append(word)
    if word == last and length <= len(ans):
        for idx in range(-1, -1-length, -1):
            if ans[idx] != key[idx]:
                break
        else:
            for _ in range(length):
                ans.pop()
if ans:
    print(''.join(ans))
else:
    print('FRULA')