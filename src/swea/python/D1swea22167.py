n = int(input())
for _ in range(n):
    string = list(input())
    new_str = []
    for i in range(len(string)-1, -1, -1):
        new_str.append(string[i])
    for char in new_str:
        print(char, end='')
    print()
