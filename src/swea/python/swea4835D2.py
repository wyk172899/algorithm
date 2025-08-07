t = int(input())
for t in range(0, t):
    n, m = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    maxNum = 0
    minNum = 3000000
    for i in range(0,len(arr) - m + 1):
        sumNum = 0
        for j in range(0,m):
            sumNum += arr[i+j]
        if sumNum > maxNum:
            maxNum = sumNum
        if sumNum < minNum:
            minNum = sumNum

    print(f"#{t+1} {maxNum - minNum}")
