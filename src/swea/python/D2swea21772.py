t = int(input())
for tc in range(t):
    n, m = list(map(int, input().split()))
    num = list(map(int, input().split()))
    for _ in range(m):
        temp = num[0]
        num.pop(0)
        num.append(temp)
    print(f"#{tc+1} {num[0]}")
