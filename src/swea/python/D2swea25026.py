t = int(input())
for tc in range(t):
    n, k = list(map(int, input().split()))
    num = list(map(int, input().split()))
    num.sort()
    max_num = 0
    for i in range(n):
        count = 1
        temp = [num[i]]
        for j in range(n):
            if i != j:
                temp.append(num[j])
                if max(temp) - min(temp) > k:
                    temp.pop()
                    continue
                count += 1
        if max_num < count:
            max_num = count
    print(f"#{tc+1} {max_num}")
