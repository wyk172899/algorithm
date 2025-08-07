t = int(input())
for t in range(0, t):
    length = int(input())
    num = [int(x) for x in list(input())]
    valid = [0] * 10
    maxIdx = 0
    for i in num:
        valid[i] += 1
    for i in range(0,10):
        if valid[i] >= valid[maxIdx]:
            maxIdx = i
    print(f"#{t+1} {maxIdx} {valid[maxIdx]}")