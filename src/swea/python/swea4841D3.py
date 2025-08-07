testcases = int(input())
for t in range(0, testcases):
    k, n, mCount = [int(x) for x in input().split()]
    m = [int(x) for x in input().split()]
    totalCount = 0
    i = 0
    while i <= n - k:
        if (i + k) == n:
            valid = True
            break
        temp = 0
        valid = False
        for j in range(k, 0, -1):
            if (i + j) in m:
                valid = True
                totalCount += 1
                temp = i + j
                break
        if not valid:
            totalCount = 0
            temp = 0
            break
        i = temp
    print(f"#{t+1} {totalCount}")
