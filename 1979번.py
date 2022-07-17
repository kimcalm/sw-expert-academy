T = int(input())

for t in range(T):
    data = []
    cnt = 0

    N, K = map(int, input().split())

    for i in range(N):
        data.append(list(map(int, input().split())))
    
    for j in range(N):
        continuous = 0
        for k in range(N):
            if data[j][k] == 1:
                continuous += 1
                if continuous == K and k+1 == N:
                    cnt += 1
                elif continuous == K and data[j][k+1] == 0:
                    cnt += 1
            else:
                continuous = 0
    
    for k in range(N):
        continuous = 0
        for j in range(N):
            if data[j][k] == 1:
                continuous += 1
                if continuous == K and j+1 == N:
                    cnt += 1
                elif continuous == K and data[j+1][k] == 0:
                    cnt += 1
            else:
                continuous = 0
    
    print('#{} {}'.format(t+1, cnt))


'''
2
5 3
0 0 1 1 1
1 1 1 1 0
0 0 1 0 0
0 1 1 1 1
1 1 1 0 1
5 3
1 0 0 1 0
1 1 0 1 1
1 0 1 1 1
0 1 1 0 1
0 1 1 1 0
'''