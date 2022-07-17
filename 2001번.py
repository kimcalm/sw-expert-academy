T = int(input())

for t in range(T):
    N, M = map(int, input().split())

    data = []
    for i in range(N):
        data.append(list(map(int, input().split())))
    
    max_value = 0
    for j in range(N-M+1):
        for k in range(N-M+1):     # M X M 매트릭스 중, 제일 왼쪽 윗점 좌표 = data[j][k]
            result = 0
            for l in range(M):
                for m in range(M):
                    result += data[j+l][k+m]

            if max_value < result:
                max_value = result
    
    print('#{} {}'.format(t+1, max_value))

'''
1
7 5
17 24 11 29 18 21 11
8 5 14 0 19 15 17
18 25 29 1 29 16 16
3 26 27 20 6 2 27
20 13 19 8 13 29 15
8 22 8 23 21 7 6
14 9 9 27 16 23 29

1
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3
6 3
29 21 26 9 5 8
21 19 8 0 21 19
9 24 2 11 4 24
19 29 1 0 21 19
10 29 6 18 4 3
29 11 15 3 3 29
'''