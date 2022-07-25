T = int(input())

for t in range(T):
    P, Q, R, S, W = map(int, input().split())

    A = W * P
    B = Q

    if W > R:
        B += (W - R) * S

    print(f'#{t+1} {min(A, B)}')



'''
2
9 100 20 3 10
8 300 100 10 250
'''