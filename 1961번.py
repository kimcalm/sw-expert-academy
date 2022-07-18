T = int(input())

for t in range(T):
    N = int(input())

    data = []
    for i in range(N):
        data.append(list(input().split()))

    new_data = []
    for j in range(N):
        value = ''
        for k in range(N-1,-1,-1):
            value += data[k][j]
        new_data.append(value)

    for j in range(N-1,-1,-1):
        value = ''
        for k in range(N-1,-1,-1):
            value += data[j][k]
        new_data.append(value)

    for j in range(N-1,-1,-1):
        value = ''
        for k in range(N):
            value += data[k][j]
        new_data.append(value)


    print('#{}'.format(t+1))

    for l in range(len(new_data)):
        if l % 3 == 0:
            print(new_data[l], end=' ')
    print()

    for l in range(len(new_data)):
        if l % 3 == 1:
            print(new_data[l], end=' ')
    print()

    for l in range(len(new_data)):
        if l % 3 == 2:
            print(new_data[l], end=' ')
    print()


'''
1
6
6 9 4 7 0 5
8 9 9 2 6 5
6 8 5 4 9 8
2 2 7 7 8 4
7 5 1 9 7 9
8 9 3 9 7 6
'''