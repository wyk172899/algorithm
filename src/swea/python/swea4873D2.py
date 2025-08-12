t = int(input())
for tc in range(t):
    string = list(input())
    l = len(string)
    newLst = []
    for i in string:
        if len(newLst) == 0:
            newLst.append(i)
        elif i == newLst[-1]:
            newLst.pop()
        else:
            newLst.append(i)
    print(f"#{tc+1} {len(newLst)}")
