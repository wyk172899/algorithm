# 블로그 참고, 원리 이해함.
t = int(input())
for tc in range(t):
    n, m = list(map(int, input().split()))
    num = list(map(int, input().split()))
    chz = []
    for i in range(m):
        chz.append([i+1, num[i]])
    ovn = chz[:n]
    left = chz[n:]
    while len(ovn) > 1:
        take = ovn.pop(0)
        take[1] //= 2
        if take[1] == 0:
            if left:
                ovn.append(left.pop(0))
        else:
            ovn.append(take)
    print(f"#{tc+1} {ovn[0][0]}")
