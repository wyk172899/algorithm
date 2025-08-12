t = int(input())
for tc in range(t):
    n = int(input())
    palette = [[0] * 10 for _ in range(10)]
    color = []
    purpleCount = 0
    for i in range(n):
        color.append(list(map(int, input().split())))
    for c in color:  # 2
        for i in range(c[0], c[2] + 1, 1):
            for j in range(c[1], c[3] + 1, 1):
                if ((palette[i][j] == 1) and (c[4] == 2)) or (
                    (palette[i][j] == 2) and (c[4] == 1)
                ):

                    palette[i][j] = 3
                else:

                    palette[i][j] = c[4]
    for i in range(10):
        for j in range(10):
            if palette[i][j] == 3:
                purpleCount += 1
    print(f"#{tc+1} {purpleCount}")
