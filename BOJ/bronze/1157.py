"""
제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
단, 대문자와 소문자를 구분하지 않는다.

입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

예제 입력 1
Mississipi
예제 출력 1
?
"""
# sol1. 딕셔너리에 알파벳 개수 저장: 시간이 오래걸렸다
word = input()
w_cnt = {}
for w in word:
    if ord('a') <= ord(w) <= ord('z'):
        w = chr(ord(w) - (ord('a')-ord('A')))

    if w_cnt.get(w):
        w_cnt[w] += 1
    else:
        w_cnt[w] = 1

cnt = max(w_cnt.values())
flag = False
for k, v in w_cnt.items():
    if cnt == v and flag:
        ans = '?'
        break
    if cnt == v:
        ans = k
        flag = True

print(ans)


# sol2. 중복값 삭제 후 세기
word = input().upper()
check_word = set(word)

num_data = []
max_v = 0
for i in check_word:
    temp = word.count(i)
    if max_v <= temp:
        max_v = temp
        ans = i
        num_data.append(temp)

if num_data.count(max_v) > 1:
    ans = '?'

print(ans)