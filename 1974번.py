T = int(input())

for t in range(T):
    data = []
    for i in range(9):
        data.append(list(map(int, input().split())))

    # 1. 행 테스트
    row_test = 1
    for row in range(9):
        if len(set(data[row])) != 9:
            row_test = 0
            break

    # 2. 열 테스트
    column_test = 1
    for column in range(9):
        lst = []
        for row in range(9):
            lst.append(data[row][column])
        if len(set(lst)) != 9:
            column_test = 0
            break

    # 3. 3 x 3 테스트
    square_test = 1

    for i in range(0, 3, 9):
        for j in range(0, 3, 9):
            lst_1 = []
            for k in range(3):
                for l in range(3):
                    lst_1.append(data[i+k][j+l])
            
            if len(set(lst_1)) != 9:
                square_test = 0
                break
        if square_test == 0:
            break

    if (row_test == 0 or column_test == 0 or square_test == 0):
        print(f'#{t+1} 0')
    else :
        print(f'#{t+1} 1')



'''
1
7 3 6 4 2 9 5 8 1
5 8 9 1 6 7 3 2 4
2 1 4 5 8 3 6 9 7
8 4 7 9 3 6 1 5 2
1 5 3 8 4 2 9 7 6
9 6 2 7 5 1 8 4 3
4 2 1 3 9 8 7 6 5
3 9 5 6 7 4 2 1 8
6 7 8 2 1 5 4 3 9
'''