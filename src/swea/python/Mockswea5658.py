t = int(input())
for tc in range(t):
    n, k = map(int, input().split())
    limit = n//4
    num = list(input())
    cal_lst = set()
    for rotate in range(limit):
        for i in range(0,n,limit):
            hex_str = ''
            for j in range(limit):
                hex_str += num[i+j]
            cal_lst.add(int(hex_str,16))
        temp = num.pop(0)
        num.append(temp)
    cal_lst = list(cal_lst)
    cal_lst.sort(reverse=True)
    print(f"#{tc+1} {cal_lst[k-1]}")
