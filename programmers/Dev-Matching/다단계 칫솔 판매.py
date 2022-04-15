"""
https://programmers.co.kr/learn/courses/30/lessons/77486
"""
def solution(enroll, referral, seller, amount):
    """
    enroll은 조직원 숫자
    referral은 enroll을 참여시킨 조직원
    seller는 판매원
    amount는 판매한 숫자 (판매액은 개당 100원)
    
    reference = { member_name : [referral_name, earn] }
    """
    answer = []
    reference = { "-": ["-", 0] }
    for k in range(len(enroll)):
        reference[enroll[k]] = [referral[k], 0]

    for k in range(len(seller)):
        cost = amount[k] * 100
        now_seller = seller[k]
        while cost:
            reference[now_seller][1] += (cost - cost//10)
            cost //= 10
            now_seller = reference[now_seller][0]
            if now_seller == "-":
                reference[now_seller][1] += cost
                break

    for k in range(len(enroll)):
        answer.append(reference[enroll[k]][1])
    return answer

print(solution(
    ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
    ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
    ["young", "john", "tod", "emily", "mary"],
    [12, 4, 2, 5, 10]
))
print(solution(
    ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
    ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
    ["sam", "emily", "jaimie", "edward"],
    [2, 3, 5, 4]
))