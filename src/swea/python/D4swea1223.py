for tc in range(1,11):
    length = int(input())
    arr = list(input())
    stack = []
    num = []
    postfix = ''
    prec = {'+': 1, '*': 2}
    for char in arr:
        if char.isdecimal():
            num.append(int(char))
            postfix += char
        else:
            while stack and prec.get(stack[-1], 0) >= prec[char]:
                postfix += stack.pop()
            stack.append(char)
    while stack:
        postfix += stack.pop()

    cal_stack = []
    for char in list(postfix):
        if char == '+':
            b = cal_stack.pop()
            a = cal_stack.pop()
            cal_stack.append(a + b)
        elif char == '*':
            b = cal_stack.pop()
            a = cal_stack.pop()
            cal_stack.append(a * b)
        else:
            cal_stack.append(int(char))

    print(f"#{tc} {cal_stack.pop()}")
