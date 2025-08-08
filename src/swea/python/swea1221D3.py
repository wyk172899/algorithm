def toNum(num):
    if num == "ZRO":
        return 0
    if num == "ONE":
        return 1
    if num == "TWO":
        return 2
    if num == "THR":
        return 3
    if num == "FOR":
        return 4
    if num == "FIV":
        return 5
    if num == "SIX":
        return 6
    if num == "SVN":
        return 7
    if num == "EGT":
        return 8
    if num == "NIN":
        return 9


def toStr(num):
    if num == 0:
        return "ZRO"
    if num == 1:
        return "ONE"
    if num == 2:
        return "TWO"
    if num == 3:
        return "THR"
    if num == 4:
        return "FOR"
    if num == 5:
        return "FIV"
    if num == 6:
        return "SIX"
    if num == 7:
        return "SVN"
    if num == 8:
        return "EGT"
    if num == 9:
        return "NIN"


t = int(input())
for tc in range(t):
    _, n = input().split()
    num = input().split()
    for i in range(int(n)):
        num[i] = toNum(num[i])
    num = sorted(num)
    for i in range(int(n)):
        num[i] = toStr(num[i])
    print(f"#{tc+1}")
    for i in range(int(n)):
        print(num[i], end=" ")
    print()

