for tc in range(10):
    n = int(input())
    num = list(map(int, input().split()))
    l = len(num)
    diff = 0
    for i in range(n):
        maxValue = 0
        maxIdx = 0
        minValue = 101
        minIdx = 0
        for j in range(l):
            if num[j] > maxValue:
                maxValue = num[j]
                maxIdx = j
            if num[j] < minValue:
                minValue = num[j]
                minIdx = j
        if maxValue == minValue:
            break
        else:
            num[maxIdx] -= 1
            num[minIdx] += 1
            diff = max(num) - min(num)
    print(f"#{tc+1} {diff}")
