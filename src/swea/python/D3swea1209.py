SIZE = 100
for t in range(0, 10):
    tc = int(input())
    maxNum = 0
    list1 = []
    for i in range(0,SIZE,1):
        list1.append([int(x) for x in input().split()])
    for i in range(0,SIZE,1):
        rowSum = 0
        colSum = 0
        for j in range(0,SIZE,1):
            rowSum += list1[i][j]
            colSum += list1[j][i]
        maxNum = max(maxNum, rowSum, colSum)
    plusStairSum = sum(list1[i][i] for i in range(SIZE))
    minusStairSum = sum(list1[i][SIZE - 1 - i] for i in range(SIZE))
    maxNum = max(maxNum, plusStairSum, minusStairSum)
    print(f"#{tc} {maxNum}".strip())
