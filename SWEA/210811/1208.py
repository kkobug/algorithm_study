def flatten():
    for tc in range(1, 11):
        N = int(input())
        box = list(map(int, input().split()))
        for i in range(N+1):
            top, bottom = 0, 100
            for b in box:
                if top < b:
                    top = b
                if bottom > b:
                    bottom = b
            if top - bottom <= 1:
                break

            # 최대값 1칸 덜기
            for j in range(len(box)):
                if box[j] >= top:
                    box[j] -= 1
                    break

            # 최소값 1칸 더하기
            for k in range(len(box)):
                if bottom >= box[k]:
                    box[k] += 1
                    break

        print("#{} {}".format(tc, top-bottom))

flatten()