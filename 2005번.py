T = int(input())

for test in range(1, T+1):
    
    N = int(input())
    data = [[] for n in range(N)]
    
    for i in range(N):
        for j in range(i+1):
            if j == 0 or j == i:
                data[i].append(1)
            else:
                data[i].append(data[i-1][j-1] + data[i-1][j])
    
    print(f'#{test}')
    for single_list in data:
        for k in single_list:
            print(k, end=' ')
        print()


'''
1
4

#1
1
1 1
1 2 1
1 3 3 1
'''