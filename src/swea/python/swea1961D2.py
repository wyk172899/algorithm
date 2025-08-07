def D90(num, origin):
    d90 = []
    for j in range(0, num):
        row = []
        for i in range(num, 0, -1):
            row.append(origin[i - 1][j])
        d90.append(row)
    return d90


def D180(num, origin):
    d180 = []
    for i in range(num, 0, -1):
        row = []
        for j in range(num, 0, -1):
            row.append(origin[i - 1][j - 1])
        d180.append(row)
    return d180


def D270(num, origin):
    d270 = []
    for j in range(num, 0, -1):
        row = []
        for i in range(0, num):
            row.append(origin[i][j - 1])
        d270.append(row)
    return d270


testcases = int(input())
for testcase in range(0, testcases):
    n = int(input())
    arr = []
    for i in range(0, n):
        arr.append([int(x) for x in input().split()])
    d90 = D90(n, arr)
    d180 = D180(n, arr)
    d270 = D270(n, arr)
    print(f"#{testcase+1}")
    for i in range(0, n):
        for j in range(0, n):
            print(d90[i][j], end="")
        print(" ", end="")
        for j in range(0, n):
            print(d180[i][j], end="")
        print(" ", end="")
        for j in range(0, n):
            print(d270[i][j], end="")
        print(" ", end="")
        print()
