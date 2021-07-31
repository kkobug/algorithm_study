def qnr():
    '''
    a를 b로 나눈 나머지
    a, b는 1이상 10000이하의 정수
    테스트케이스 개수 T
    '''
    T = int(input())
    
    deno_nume = []
    for i in range(T):
        deno_nume.append(list(map(int, input().split(' '))))
    
    for j in range(T):
        print(f'#{j+1} {deno_nume[j][0]//deno_nume[j][1]} {deno_nume[j][0]%deno_nume[j][1]}')

qnr()