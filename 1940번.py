T = int(input())

for t in range(T):
    N = int(input())

    dis = 0
    vel = 0
    for n in range(N):
        data = list(map(int, input().split()))

        if data[0] == 1:
            vel += data[1]
        elif data[0] == 2:
            if vel < data[1]:
                continue
            vel -= data[1]

        dis += vel

    print(f'#{t+1} {dis}')
        




'''
1
25
2 1
2 1
0
0
0
1 2
0
2 2
1 2
2 1
1 1
2 1
0
0
0
1 1
1 2
0
0
1 2
2 2
0
2 2
0
1 1

1
30
2 1
2 2
2 2
1 1
1 2
2 1
0
1 1
0
0
1 2
1 2
2 1
0
0
2 2
2 1
1 2
0
1 1
2 2
1 2
2 2
0
1 2
2 1
2 2
0
1 1
2 2
'''