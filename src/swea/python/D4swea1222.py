for tc in range(1,11):
    length = int(input())
    arr = list(input())
    stack = []
    num = []
    postfix = ''
    for char in arr:
        if char == '+':
            while stack:
                postfix += stack.pop()
            stack.append('+')
        else:
            num.append(int(char))
            postfix += char
    while stack:
        postfix += stack.pop()
    print(f"#{tc} {sum(num)}")