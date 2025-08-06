t = int(input())
for t in range(0, t):
    length = int(input())
    num = [int(x) for x in input().split()]
    minNum = 1000000
    maxNum = 0
    for i in num:
        if i >= maxNum:
            maxNum = i
        if i <= minNum:
            minNum = i
    print(f"#{t+1} {maxNum - minNum}")
