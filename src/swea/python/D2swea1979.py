t = int(input())
for tc in range(t):
    n, m = list(map(int, input().split()))
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    count = 0
    for i in range(n):
        row_count = 0
        col_count = 0
        for j in range(n):

            if arr[i][j] == 1:
                row_count += 1
            elif arr[i][j] == 0:
                if row_count == m:
                    count += 1
                    row_count = 0
                else:
                    row_count = 0

            if arr[j][i] == 1:
                col_count += 1
            elif arr[j][i] == 0:
                if col_count == m:
                    count += 1
                    col_count = 0
                else:
                    col_count = 0
        if row_count == m:
            count += 1
        if col_count == m:
            count += 1
    print(f"#{tc+1} {count}")
