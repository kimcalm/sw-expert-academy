T = int(input())

for i in range(T):
    N = int(input())
    data = [input().split() for j in range(N)]

    lst = []
    for j in data:
        for k in range(int(j[1])):
            lst.append(j[0])

    print('#{}'.format(i+1))

    for l in range(len(lst)):
        print(lst[l], end='')
        if l % 10 == 9:
            print()
    print()