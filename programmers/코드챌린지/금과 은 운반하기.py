def solution(a, b, g, s, w, t):
    answer = 5*(10**14)
    N = len(t)
    # a : 필요한 금
    # b : 필요한 은
    # g : 도시별 보유 금 무게
    # s : 도시별 보유 은 무게
    # w : 도시별 운반 가능 무게
    # t : 도시별 운반 편도 시간
    st = 0
    ed = answer
    
    while st <= ed:
        mid = (st + ed) // 2
        gold = silver = total = 0
        
        for i in range(N):
            move_cnt = mid // t[i]          # move_cnt번 움직일 수 있음
            move_cnt = (move_cnt + 1) // 2  # 운반 가능횟수는 그 절반의 반올림
            
            # 금 싣기
            if g[i] < move_cnt * w[i]:
                gold += g[i]
            else:
                gold += move_cnt * w[i]
            
            # 은 싣기
            if s[i] < move_cnt * w[i]:
                silver += s[i]
            else:
                silver += move_cnt * w[i]
            
            # 광물이 너무 많아요
            if g[i] + s[i] < move_cnt * w[i]:
                total += g[i] + s[i]
            else:
                total += move_cnt * w[i]
        
        if a <= gold and b <= silver and a + b <= total:
            ed = mid - 1
            answer = min(answer, mid)
        else:
            st = mid + 1
    return answer


print(solution(10, 10, [100], [100], [7], [10]))
print(solution(90, 500, [70,70,0], [0,0,500], [100,100,2], [4,8,1]))
print(solution(200, 200, [300, 100], [0, 200], [200, 200], [1, 1]))
print(solution(200, 200, [100, 300], [200, 0], [200, 200], [1, 1]))
