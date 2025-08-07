t = int(input())
for tc in range(t):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    sortedArr = []
    for i in range(n//2):
        sortedArr.append(arr[n - 1 - i])
        sortedArr.append(arr[i])
    string1 = f"# {tc+1} "
    for i in range(10):
        string1 += f"{sortedArr[i]} "
    print(string1.strip())