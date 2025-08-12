testcases = int(input())
for testcase in range(0, testcases):
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    isaLonger = True if len(a) > len(b) else False
    if isaLonger:
        maxOfNum = 0
        for i in range(0, len(a) - len(b) + 1):
            sumOfNum = 0
            for j in range(0, len(b)):
                sumOfNum = sumOfNum + a[i + j] * b[j]
            if maxOfNum < sumOfNum:
                maxOfNum = sumOfNum
        print(f"#{testcase+1} {maxOfNum}")
    else:
        maxOfNum = 0
        for i in range(0, len(b) - len(a) + 1):
            sumOfNum = 0
            for j in range(0, len(a)):
                sumOfNum = sumOfNum + b[i + j] * a[j]
            if maxOfNum < sumOfNum:
                maxOfNum = sumOfNum
        print(f"#{testcase+1} {maxOfNum}")

# 97~122 26
# [int(x) for x in input().split()]
# if(a[ord(s[j+1])-97] == 1):
#                 t -= 1
#             else:
