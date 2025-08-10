for tc in range(10):
    t = int(input())
    data = []
    for _ in range(100):
        data.append(list(map(int, input().split())))
    minNum = 100000
    minIdx = -1
    for x in range(100):
        if data[0][x] != 1:
            continue
        i, j = 0, x
        length = 0
        while i < 99:
            if j > 0 and data[i][j - 1] == 1:
                while j > 0 and data[i][j - 1] == 1:
                    j -= 1
                    length += 1
                i += 1
                length += 1
            elif j < 99 and data[i][j + 1] == 1:
                while j < 99 and data[i][j + 1] == 1:
                    j += 1
                    length += 1
                i += 1
                length += 1
            else:
                i += 1
                length += 1
        if length < minNum:
            minNum = length
            minIdx = x
    print(f"#{tc+1} {minIdx}")