def valid_process(lst, string_length):
    if string_length % 2 != 0:
        return lst[: (string_length // 2) + 1:] == lst[-1: -((string_length // 2) + 2): -1]
    else:
        return lst[: string_length // 2:] == lst[-1: (string_length // 2) - 1: -1]


for tc in range(10):
    length = int(input())
    words = []
    count = 0
    for i in range(8):
        words.append(list(input()))
    for i in range(8):
        for t in range(8 - length + 1):
            rowTemp = []
            colTemp = []
            for j in range(length):
                rowTemp.append(words[i][j + t])
                colTemp.append(words[j + t][i])
            if valid_process(rowTemp, length):
                answer = rowTemp
                count += 1
            if valid_process(colTemp, length):
                answer = colTemp
                count += 1
    print(f"#{tc+1} {count}")
