for testcases in range(0, 10):
    buildingCount = int(input())
    buildingHeight = [int(x) for x in input().split()]
    totalDiff = 0
    for i in range(2, buildingCount - 2):
        valid = False
        diff = 255
        for j in range(i, i + 5, 1):
            sub = buildingHeight[i] - buildingHeight[j - 2]
            if (buildingHeight[i] > buildingHeight[j - 2]) and (diff > sub):
                diff = sub
            elif (buildingHeight[i] <= buildingHeight[j - 2]) and (i != j - 2):
                valid = True
        if not valid:
            totalDiff += diff
    print(f"#{testcases+1} {totalDiff}")
