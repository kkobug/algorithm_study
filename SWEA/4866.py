def isbraket(word):
    stack = []
    for w in word:
        if w in "({":
            stack.append(w)

        elif w in ")}":
            if stack:
                if (w == ")" and stack[-1] == "(") or (w == "}" and stack[-1] == "{"):
                    stack.pop()
                else: return 0
            else: return 0

    if stack:
        return 0
    return 1


for tc in range(1, 1+int(input())):
    word = input()
    print("#{} {}".format(tc, isbraket(word)))