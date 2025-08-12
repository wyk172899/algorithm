t = int(input())
for tc in range(t):
    string = list(input())
    stack = []
    dict1 = {"{": "}", "(": ")"}
    valid = False
    for ch in string:
        if (ch == "{") or (ch == "("):
            stack.append(ch)
        elif (ch == "}") or (ch == ")"):
            if stack:
                if ch == dict1[stack[-1]]:
                    stack.pop()
                else:
                    valid = True
            else:
                valid = True
    if valid:
        print(f"#{tc + 1} 0")
    elif not stack:
        print(f"#{tc+1} 1")
    else:
        print(f"#{tc+1} 0")
