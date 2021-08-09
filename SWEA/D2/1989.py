def palindrome():
    T = int(input())
    word = []
    for i in range(T):
        word.append(input())
    
    cnt = 0
    for w in word:
        cnt += 1
        if w == w[::-1]:
            print(f'#{cnt} 1')
        else:
            print(f'#{cnt} 0')

palindrome()