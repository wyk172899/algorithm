for tc in range(10):
    t = input()
    num = list(map(int, input().split()))
    i = 0
    while num[7]:
        i = (i % 5) + 1
        if num[0] - i <= 0:
            num.pop(0)
            num.append(0)
            break
        temp = num[0]
        num.pop(0)
        num.append(temp - i)
    ans = ' '.join(map(str, num))
    print(f"#{t} {ans}")
