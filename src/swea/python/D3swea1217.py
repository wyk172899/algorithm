def square(n, s):
    total = n
    if s == 1:
        return n
    total *= square(n, s-1)
    return total


for _ in range(10):
    tc = input()
    n, s = list(map(int, input().split()))
    print(f"#{tc} {square(n, s)}")
