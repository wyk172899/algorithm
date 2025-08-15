t = int(input())
for tc in range(1,t+1):
    n = int(input())
    c = list(map(int, input().split()))
    temp = []
    count = 1
    for i in range(n):
        if i == n-1:
            temp.append(count)
            break
        elif c[i] < c[i+1]:
            count += 1
        else:
            temp.append(count)
            count = 1
    print(f"#{tc} {max(temp)}")