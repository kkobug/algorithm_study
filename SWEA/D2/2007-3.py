T = int(input())
user_input = []
for test_case in range(T):
    user_input.append(input())

ans = []

for words in user_input:
    for i in range(1, len(words) // 2):
        word = words[0:i]
        if word * (len(words) // (i)) in words:
            ans.append(word)
            break
        # elif word == words[i:i*2] and i <= len(words) // 4:
        #     temp = word * 2
        #     if temp * (len(words) // (i * 2)) in words:
        #         ans.append(temp)
        #         break
            
for i in range(len(ans)):
    print(f'#{i+1} {len(ans[i])}')
