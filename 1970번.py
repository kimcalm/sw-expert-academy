T = int(input())

money_unit = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for t in range(T):
    N = int(input())

    print(f'#{t+1}')    
    for unit in money_unit:
        cnt = N // unit
        N -= cnt * unit
        print(f'{cnt}', end=' ')

    print()

'''
2 
32850
160     
'''