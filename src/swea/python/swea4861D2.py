def validProcess(lst, len):
    if m % 2 != 0:
        return lst[: (len // 2) + 1 :] == lst[-1 : -((len // 2) + 2) : -1]
    else:
        return lst[: len // 2 :] == lst[-1 : (len // 2) - 1 : -1]


t = int(input())
for tc in range(t):
    n, m = list(map(int, input().split()))
    words = []
    answer = []
    valid = False
    for i in range(n):
        words.append(list(input()))
    for i in range(n):
        if valid:
            break
        for t in range(n - m + 1):
            rowTemp = []
            colTemp = []
            for j in range(m):
                rowTemp.append(words[i][j + t])
                colTemp.append(words[j + t][i])
            if validProcess(rowTemp, m):
                answer = rowTemp
                valid = True
            elif validProcess(colTemp, m):
                answer = colTemp
                valid = True
    answer = "".join(answer)
    print(f"#{tc+1} {answer}")
