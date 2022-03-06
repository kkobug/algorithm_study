def solution(n, info):
    answer = [-1]
    check = [0] * 11
    max_gap = -1
    min_cnt = 0
    min_val = 10
    
    def get_score(target):
        apeach = brown = 0
        for i in range(11):
            if info[i] or target[i]:
                if info[i] < target[i]:
                    brown += 10-i
                else:
                    apeach += 10-i
        return brown - apeach

    def get_minimum(target):
        val = cnt = 0
        for i in range(10, -1, -1):
            if target[i]:
                val = 10-i
                cnt = target[i]
                return val, cnt
        return val, cnt

    def shot(now_target=0, ammo=n):
        nonlocal n, max_gap, answer, min_val, min_cnt
        if ammo == 0 or now_target == 11:
            if now_target == 11:
                check[10] += ammo
            gap = get_score(check)
            if 0 < gap:
                min_val_, min_cnt_ = get_minimum(check)
                if max_gap < gap:
                    min_val = min_val_
                    min_cnt = min_cnt_
                    max_gap = gap
                    answer = check[:]
                elif max_gap == gap:
                    if min_val_ < min_val:
                        min_val = min_val_
                        min_cnt = min_cnt_
                        answer = check[:]
                    elif min_val == min_val_:
                        if min_cnt < min_cnt_:
                            min_cnt = min_cnt_
                            answer = check[:]
            if now_target == 11:
                check[10] -= ammo
            return


        for i in range(now_target, 11):
            if info[i] < ammo:
                need_fire = info[i] + 1
                check[i] += need_fire
                shot(i+1, ammo-need_fire)
                check[i] -= need_fire
            else:
                shot(i+1, ammo)
    
    shot()
    return answer

n = 9
info = [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]
print(solution(n, info))