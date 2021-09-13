"""
<쇠막대기>
https://www.acmicpc.net/problem/10799
예제 입력 1
()(((()())(())()))(())
예제 출력 1
17
"""
laser = input()
bar = ans = i = 0
length = len(laser)

while i < length:
    if laser[i] == "(":
        if laser[i+1] == ")":
            ans += bar
            i += 1
        else:
            bar += 1
    else:
        ans += 1
        bar -= 1
    i += 1
print(ans)